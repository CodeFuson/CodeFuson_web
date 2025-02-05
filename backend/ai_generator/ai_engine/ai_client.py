from openai import OpenAI
from .prompt_generator import generate_prompt


def generate_code_from_ai(prompt: str, faiss_index, api_key: str, base_url: str) -> str:

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
        return response.choices[0].message.content
    return ""
