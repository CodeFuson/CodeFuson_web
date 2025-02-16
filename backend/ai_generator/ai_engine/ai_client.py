import re
from openai import OpenAI
from .prompt_generator import generate_prompt


def generate_code_from_ai(prompt: str, faiss_index, api_key: str, base_url: str) -> dict:
    """Generates JavaScript and CSS code using OpenAI's API."""

    client = OpenAI(api_key=api_key, base_url=base_url)
    full_prompt = generate_prompt(prompt, faiss_index,)

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": full_prompt},
            ],
            stream=False
        )

        if not response.choices or not response.choices[0].message.content:
            return {"js": "", "css": ""}

        generated_code = response.choices[0].message.content.strip()

        # Extract JS and CSS using regex
        js_match = re.search(r"/\* JS START \*/(.*?)/\* JS END \*/", generated_code, re.DOTALL)
        css_match = re.search(r"/\* CSS START \*/(.*?)/\* CSS END \*/", generated_code, re.DOTALL)

        return {
            'js': js_match.group(1).strip() if js_match else "",
            'css': css_match.group(1).strip() if css_match else ""
        }

    except Exception as e:
        print(f"Error in AI code generation: {e}")
        return {"js": "", "css": ""}
