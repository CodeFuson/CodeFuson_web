import os

from ai_generator.read_file import read_file


def generate_dockerfile(frontend_folder: str, template_path: str = "ai_generator/template/Dockerfile-template"):
    """Generates the Dockerfile from a template."""
    dockerfile_content = read_file(template_path)

    output_path = os.path.join(frontend_folder, "Dockerfile")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dockerfile_content)

    print(f"Dockerfile generated at: {output_path}")
