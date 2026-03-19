from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # very stable on free tier
    task="text-generation",

)
model = ChatHuggingFace(llm=llm)
result = model.invoke("Tell me an incredible joke")
print(result.content)  # .content to print just the text