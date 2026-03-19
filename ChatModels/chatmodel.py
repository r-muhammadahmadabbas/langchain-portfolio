from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model=ChatGoogleGenerativeAI(model='models/gemini-2.5-flash-lite',temperature = 2.0)

result = model.invoke("Write a 5 liner upwork propsal for genai expert that must bring me order")

print(result.content)