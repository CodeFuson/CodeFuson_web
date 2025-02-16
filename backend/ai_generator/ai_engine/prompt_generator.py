import os
from ai_generator.read_file import read_file

def generate_prompt(prompt: str, faiss_index, rules_file="ai_generator/template/rules.txt") -> str:
    """Generates a prompt using FAISS search results and predefined rules from a file."""

    # Search in the FAISS index
    query = faiss_index.similarity_search(prompt, k=3)
    relevant_components = "\n".join([doc.page_content for doc in query])

    # Get the absolute path of the rules file
    absolute_rules_path = os.path.abspath(rules_file)

    # Read rules from file
    base_rules = read_file(absolute_rules_path)

    # Build full prompt
    full_prompt = f"""
Relevant Components:
{relevant_components}

Please follow these rules while generating the code:
{base_rules}

Task: {prompt}
    """

    return full_prompt
