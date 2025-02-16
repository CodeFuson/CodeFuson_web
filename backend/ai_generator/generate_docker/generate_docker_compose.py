import os

from ai_generator.read_file import read_file


def generate_docker_compose(folder: str, template_path: str = "ai_generator/template/docker-compose-template.yml"):
    """Generates the docker-compose.yml file from a template."""
    docker_compose_content = read_file(template_path)

    output_path = os.path.join(folder, "docker-compose.yml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(docker_compose_content)

    print(f"Docker Compose file generated at: {output_path}")
