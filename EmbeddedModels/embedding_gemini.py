from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensions = 32)
# result = embeddings.embed_query("Islamabad is capital of pakistan")#for creation of embedding for one
#for docs
documents = [
    "Islamabad is capital of Pakistan",
    "Karachi is capital of sindh",
    "Quetta is capital of balochistan"
]
result=embeddings.embed_documents(documents)

print(result)