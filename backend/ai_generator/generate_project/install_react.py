import os
import subprocess


def install_react(project_path):
    frontend_path = os.path.join(project_path, "frontend")

    if os.path.exists(frontend_path):
        print("React frontend already exists. Skipping installation.")
        return


    try:
        # Run npx to create the React app
        result = subprocess.run(
            f"npx create-react-app {frontend_path}",
            shell=True, check=True, text=True, capture_output=True
        )

    except subprocess.CalledProcessError as e:
        print(e.stderr)
        raise e