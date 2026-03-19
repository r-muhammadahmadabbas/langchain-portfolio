from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="models/gemini-2.5-flash-lite"
)

result = llm.invoke("What is the capital of Pakistan?")
print(result)