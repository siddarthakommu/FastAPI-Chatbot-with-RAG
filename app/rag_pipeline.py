import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from app.utils.logger import logger
import openai  # ✅ Using OpenAI SDK for UltraSafe

load_dotenv()


openai.api_key = os.getenv("ULTRASAFE_API_KEY")
openai.base_url = os.getenv("ULTRASAFE_BASE_URL")


embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", cache_folder="./model_cache")
persist_directory = "chromadb_store"
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

def query_rag_pipeline(query: str):
    try:
        docs = vectordb.similarity_search(query, k=2)
        context = " ".join([doc.page_content for doc in docs])

        print("Retrieved Context:\n", context[:300])

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": f"Use this context: {context}"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Exception occurred: {str(e)}"

