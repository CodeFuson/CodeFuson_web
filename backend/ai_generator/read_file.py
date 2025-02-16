def read_file(filepath):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {filepath} not found.")
        return ""
