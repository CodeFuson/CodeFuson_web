import os


def generate_docker_compose(folder):
    docker_compose_content = f"""
    version: "3.8"
    services:
      frontend:
        build:
          context: ./frontend
        ports:
          - "3001:3000"
        volumes:
          - ./frontend:/app
        environment:
          - NODE_ENV=development
    """

    with open(os.path.join(folder, "docker-compose.yml"), "w") as f:
        f.write(docker_compose_content)
