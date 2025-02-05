def generate_prompt(prompt: str, faiss_index) -> str:

    query = faiss_index.similarity_search(prompt, k=3)
    relevant_components = "\n".join([doc.page_content for doc in query])

    base_rules = """
1. Try to use available components most of the time.
2. Ensure the generated code is clear, readable, and maintainable.
3. Organize all code into functions and avoid inline structures.
4. Never use global variables; pass all data explicitly through function parameters.
5. Follow user instructions precisely.
6. The generated code must be free of syntax, runtime, and logical errors.
7. Implement robust error handling with detailed messages.
8. Follow Python best practices.
9. Reuse existing components to avoid repetition.
10. Optimize code performance.
11. Validate the generated code for immediate execution.
12. Include only necessary imports.
13. Document complex logic.
14. Keep functions modular and reusable.
15. Avoid deeply nested loops.
16. Optimize resource usage.
17. Use descriptive variable names.
18. Provide docstrings for every function.
19. Validate and sanitize input.
20. Keep solutions straightforward.
21. Write only Python code.
22. Ensure the code ends with a main() function.
    """

    full_prompt = f"""
Relevant Components:
{relevant_components}

Please follow these rules while generating the code:
{base_rules}

Task: {prompt}
    """

    return full_prompt
