import os
def generate_folder():
    project_dir = "/codefusion/GeneratedProjects"
    os.makedirs(project_dir, exist_ok=True)
    # Determine the next project number
    existing_projects = [name for name in os.listdir(project_dir)
                         if os.path.isdir(os.path.join(project_dir, name)) and not name.startswith('.')]
    next_project_number = len(existing_projects) + 1
    project_folder_name = f"{next_project_number}_Project"
    project_path = os.path.join(project_dir, project_folder_name)
    os.makedirs(project_path, exist_ok=True)
    return project_path