import os
import logging
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_components_to_faiss(directories, index_name="components_index",
                             embedding_model="sentence-transformers/all-MiniLM-L6-v2"):
    """Loads Python files from specified directories, creates FAISS index with text embeddings."""

    docs = []
    file_paths = []

    for directory_path in directories:
        if not os.path.exists(directory_path):
            logging.warning(f"Directory does not exist: {directory_path}")
            continue

        for filename in os.listdir(directory_path):
            if filename.endswith(".py"):
                file_path = os.path.join(directory_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        logging.info(f"Loaded: {filename} ({len(content)} characters)")
                        docs.append(content)
                        file_paths.append(file_path)
                except Exception as e:
                    logging.error(f"Error loading {file_path}: {e}")

    if not docs:
        raise ValueError("No valid Python components found in the specified directories.")

    logging.info(f"Using embedding model: {embedding_model}")
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)

    # FAISS index létrehozása és mentése
    faiss_index = FAISS.from_texts(docs, embeddings)
    faiss_index.save_local(index_name)

    logging.info(f"FAISS index saved as: {index_name}")
    return faiss_index
