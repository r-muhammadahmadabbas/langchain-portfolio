from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

text = "Islamabad is the capital of pakistan "

vector = embedding.embed_query(text)
print(str(vector))