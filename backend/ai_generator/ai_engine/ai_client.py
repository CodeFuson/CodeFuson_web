from openai import OpenAI
from .prompt_generator import generate_prompt


def generate_code_from_ai(prompt: str, faiss_index, api_key: str, base_url: str) -> dict:
    client = OpenAI(api_key=api_key, base_url=base_url)
    full_prompt = generate_prompt(prompt, faiss_index)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt},
        ],
        stream=False
    )

    if response.choices:
        generated_code = response.choices[0].message.content

        # Now, separate the JS and CSS parts from the generated code
        # You can split the returned content based on a delimiter or a specific structure
        js_code = ""
        css_code = ""

        # Assuming you can parse the code into JS and CSS (adjust as necessary)
        if "/* JS START */" in generated_code and "/* JS END */" in generated_code:
            js_code = generated_code.split("/* JS START */")[1].split("/* JS END */")[0]

        if "/* CSS START */" in generated_code and "/* CSS END */" in generated_code:
            css_code = generated_code.split("/* CSS START */")[1].split("/* CSS END */")[0]

        return {
            'js': js_code.strip(),
            'css': css_code.strip()
        }

    return {"js": "", "css": ""}
