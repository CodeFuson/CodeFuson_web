import os
from ai_engine.faiss_index import load_components_to_faiss
from ai_engine.prompt_generator import generate_prompt
from ai_engine.ai_client import generate_code_from_ai


def save_generated_project(generated_code):
    projects_dir = os.path.join(os.getcwd(), "..", "projects")

    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    existing_projects = [name for name in os.listdir(projects_dir)
                         if os.path.isdir(os.path.join(projects_dir, name))]
    next_project_number = len(existing_projects) + 1
    project_folder_name = f"{next_project_number}_Projekt"
    project_path = os.path.join(projects_dir, project_folder_name)

    os.makedirs(project_path, exist_ok=True)

    output_file = os.path.join(project_path, "generated_code.py")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(generated_code)

    print(f"Generated project saved to: {project_path}")
    return project_path


def main(prompt):

    component_directories = ["./components"]  # A 'components' mappa a projekt gyökérében van
    index_name = "components_index"

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = "https://api.deepseek.com"

    try:
        faiss_index = load_components_to_faiss(component_directories, index_name)

        full_prompt = generate_prompt(prompt, faiss_index)

        generated_code = generate_code_from_ai(prompt, faiss_index, api_key, base_url)
        print("Generated Code:")
        print(generated_code)

        save_generated_project(generated_code)

        return generated_code

    except Exception as e:
        print(f"Error in main: {e}")
        raise e


if __name__ == "__main__":
    user_prompt = input("Enter what you want your software to do: ")
    main(user_prompt)
