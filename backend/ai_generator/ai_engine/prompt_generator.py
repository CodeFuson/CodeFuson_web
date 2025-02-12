def generate_prompt(prompt: str, faiss_index) -> str:

    query = faiss_index.similarity_search(prompt, k=3)
    relevant_components = "\n".join([doc.page_content for doc in query])

    base_rules = """
        1. Try to use available components most of the time.
        2. Ensure the generated code is clear, readable, and maintainable.
        3. Organize the code into functional React components.
        4. Use functional components and hooks wherever possible.
        5. Avoid using class components.
        6. Ensure separation of concerns: separate JS logic, JSX, and CSS styles.
        7. Write modular CSS and avoid inline styles.
        8. Follow user instructions precisely and keep the task-oriented.
        9. Avoid using unnecessary libraries or dependencies.
        10. Ensure the code is production-ready, efficient, and optimized.
        11. The generated code should be free of syntax, runtime, and logical errors.
        12. Use descriptive class names and variable names.
        13. Provide comments and document the code where necessary.
        14. Write the React component in a functional style with hooks (useState, useEffect, etc.).
        15. Include a `main()` function or equivalent entry point in the code.
        16. The generated JS code should be enclosed within the markers: /* JS START */ and /* JS END */.
        17. The generated CSS code should be enclosed within the markers: /* CSS START */ and /* CSS END */.
        18. The generated code must be compatible with the latest version of React.
        19. Avoid deeply nested structures or excessive abstraction.
        20. The generated JS file must always be named `Home.js` and the CSS file must always be named `Home.css`.
    """

    full_prompt = f"""
Relevant Components:
{relevant_components}

Please follow these rules while generating the code:
{base_rules}

Task: {prompt}
    """

    return full_prompt
