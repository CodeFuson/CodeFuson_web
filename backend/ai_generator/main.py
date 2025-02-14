import os

from django.http.response import JsonResponse
from dotenv import load_dotenv

from ai_generator.generate_project.generate_folder import generate_folder
from ai_generator.generate_project.install_react import install_react
from ai_generator.generate_project.save_react_code import save_generated_react_code

load_dotenv()

from .ai_engine.faiss_index import load_components_to_faiss
from .ai_engine.ai_client import generate_code_from_ai


def main(prompt):
    component_directories = ["./components"]
    index_name = "components_index"

    api_key = os.getenv("OPENAI_API_KEY")

    base_url = "https://api.deepseek.com"

    try:
        faiss_index = load_components_to_faiss(component_directories, index_name)

        generated_code = generate_code_from_ai(prompt, faiss_index, api_key, base_url)

        folder = generate_folder()

        install_react(folder)

        save_generated_react_code(generated_code, folder)

        return JsonResponse({"code": generated_code})

    except Exception as e:
        print(f"Error in main: {e}")
        raise e


if __name__ == "__main__":
    user_prompt = input("Enter what you want your software to do: ")
    main(user_prompt)
