import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load env (optional)
load_dotenv()


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
    cache_folder="./model_cache"
)



docs = []
for filename in os.listdir("support_docs"):
    if filename.endswith(".txt") or filename.endswith(".md"):
        loader = TextLoader(os.path.join("support_docs", filename))
        docs.extend(loader.load())


splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)


vectordb = Chroma.from_documents(documents=chunks, embedding=embedding, persist_directory="chromadb_store")
vectordb.persist()

print("Documents embedded using Hugging Face and saved to ChromaDB.")


