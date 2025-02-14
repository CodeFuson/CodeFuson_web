import subprocess

from django.http.response import JsonResponse


def run_docker_compose(folder):
    """Run docker-compose to build and start the containers"""
    try:
        result = subprocess.run(
            ["docker-compose", "-f", os.path.join(folder, "docker-compose.yml"), "up", "-d"],
            check=True,
            text=True,
            capture_output=True
        )
        print("Docker Compose Output:", result.stdout)
        return JsonResponse({"message": "Project started successfully!"})
    except subprocess.CalledProcessError as e:
        print("Error running Docker Compose:", e.stderr)
        return JsonResponse({"error": "Failed to start the project."})
