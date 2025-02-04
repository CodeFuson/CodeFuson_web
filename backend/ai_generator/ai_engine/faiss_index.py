from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

def load_components_to_faiss(directories, index_name="components_index",
                             embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
    docs = []
    for directory_path in directories:
        if not os.path.exists(directory_path):
            print(f"Warning: Directory does not exist: {directory_path}")
            continue

        for filename in os.listdir(directory_path):
            if filename.endswith(".py"):
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        print(f"Loaded document: {filename}, Length: {len(content)} characters")
                        docs.append(content)
                except Exception as e:
                    print(f"Error loading file {file_path}: {e}")

    if not docs:
        raise ValueError("No valid components found in the specified directories.")

    print(f"Using embedding model: {embedding_model}")
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    faiss_index = FAISS.from_texts(docs, embeddings)
    faiss_index.save_local(index_name)
    print(f"FAISS index saved locally as: {index_name}")
    return faiss_index
