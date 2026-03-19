from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimensionb = 300)

documents = [
    "Large Language Models (LLMs) use transformer architectures to predict the next token in a sequence.",
    "DevOps bridges the gap between software development and IT operations through continuous integration.",
    "Quantum computing leverages superposition and entanglement to perform complex calculations.",
    "FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+.",
    "Edge computing processes data closer to the source to reduce latency and bandwidth usage.",
    "Reinforcement Learning involves an agent taking actions in an environment to maximize cumulative rewards."
]

query = 'tell me about llms '

user_embeddings=embedding.embed_query(query)
doc_embeddings=embedding.embed_documents(documents)

sim_score = cosine_similarity([user_embeddings],doc_embeddings)[0]

index,score = sorted(list(enumerate(sim_score)),key=lambda x:x[1])[-1]
print(documents[index])
print("Similarity score is:", score)