import subprocess


def install_frontend_dependencies(frontend_folder):
    """Run npm install in the frontend folder"""
    try:
        result = subprocess.run(
            ["npm", "install"],
            cwd=frontend_folder,
            check=True,
            text=True,
            capture_output=True
        )
        print("NPM Install Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error during NPM install:", e.stderr)
        raise e
