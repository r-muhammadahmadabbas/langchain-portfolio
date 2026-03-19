# 🦜 LangChain Portfolio

A hands-on portfolio of LangChain experiments and implementations covering Chat Models, Embedding Models, and Large Language Models (LLMs). This repository serves as a practical reference for working with multiple AI providers — Google Gemini, OpenAI, and Hugging Face — through the LangChain framework.

---

## 📁 Project Structure

```
langchain-portfolio/
├── ChatModels/
│   ├── chatmodel.py         # Google Gemini chat via LangChain
│   ├── hf_api.py            # Hugging Face Inference API (cloud)
│   └── hf_local.py          # Hugging Face local pipeline (on-device)
├── EmbeddedModels/
│   ├── embedding_gemini.py  # Gemini embeddings for documents
│   ├── embedding_hf.py      # Hugging Face sentence embeddings
│   └── project.py           # Semantic search using cosine similarity
├── LLMs/
│   └── basic_chatbot.py     # Simple LLM chatbot with Gemini
├── .gitignore
├── requirements.txt
└── test.py                  # LangChain version check
```

---

## 🧩 Module Breakdown

### 💬 ChatModels

Demonstrates integrating chat-oriented LLMs through LangChain's unified interface.

| File | Description |
|------|-------------|
| `chatmodel.py` | Uses `ChatGoogleGenerativeAI` with `gemini-2.5-flash-lite` to generate a 5-line Upwork proposal. Configures `temperature=2.0` for creative outputs. |
| `hf_api.py` | Connects to Hugging Face's Inference API using `HuggingFaceEndpoint` with `TinyLlama/TinyLlama-1.1B-Chat-v1.0` — suitable for the free tier. |
| `hf_local.py` | Runs TinyLlama locally via `HuggingFacePipeline` with a `text-generation` task and configurable `temperature` and `max_new_tokens`. |

---

### 🔢 EmbeddedModels

Explores text embedding techniques across different providers for use in semantic search and retrieval tasks.

| File | Description |
|------|-------------|
| `embedding_gemini.py` | Generates low-dimensional (32-dim) vector embeddings for multiple documents using Google's `gemini-embedding-001` model. |
| `embedding_hf.py` | Creates embeddings using `sentence-transformers/all-MiniLM-L6-v2` via `HuggingFaceEmbeddings` — a lightweight, local option. |
| `project.py` | Builds a mini semantic search engine: embeds a query and 6 documents using Gemini, then ranks results by **cosine similarity** using `scikit-learn`. |

---

### 🤖 LLMs

Foundational LLM usage with Google Gemini.

| File | Description |
|------|-------------|
| `basic_chatbot.py` | Invokes `GoogleGenerativeAI` with `gemini-2.5-flash-lite` to answer a simple factual question — a clean starting point for LLM integration. |

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/r-muhammadahmadabbas/langchain-portfolio.git
cd langchain-portfolio
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
OPENAI_API_KEY=your_openai_api_key_here   # if needed
```

> **Note:** The `.env` file is listed in `.gitignore` and will not be committed to version control.

---

## 🚀 Running the Scripts

```bash
# Verify LangChain installation
python test.py

# Run a chat model example
python ChatModels/chatmodel.py

# Run a Hugging Face cloud model
python ChatModels/hf_api.py

# Run a Hugging Face local model (downloads model on first run)
python ChatModels/hf_local.py

# Generate Gemini embeddings
python EmbeddedModels/embedding_gemini.py

# Generate Hugging Face embeddings
python EmbeddedModels/embedding_hf.py

# Run the semantic search project
python EmbeddedModels/project.py

# Run the basic LLM chatbot
python LLMs/basic_chatbot.py
```

---

## 🛠️ Tech Stack

| Category | Libraries |
|----------|-----------|
| **LLM Framework** | `langchain`, `langchain-core` |
| **Google AI** | `langchain-google-genai`, `google-generativeai`, `google-genai` |
| **Hugging Face** | `langchain-huggingface`, `transformers`, `sentence-transformers`, `huggingface_hub` |
| **OpenAI** | `langchain-openai`, `openai` |
| **ML / Similarity** | `scikit-learn`, `numpy` |
| **Utilities** | `python-dotenv` |

---

## 🔑 API Keys Required

| Provider | Where to Get |
|----------|-------------|
| Google Gemini | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| Hugging Face | [HuggingFace Settings](https://huggingface.co/settings/tokens) |
| OpenAI (optional) | [OpenAI Platform](https://platform.openai.com/api-keys) |

---

## 📌 Key Concepts Covered

- **Chat Models vs. LLMs** — Understanding the difference between instruction-tuned chat models and raw completion LLMs in LangChain
- **Embedding Models** — Converting text into vector representations for downstream tasks
- **Semantic Search** — Using cosine similarity to find the most relevant document for a given query
- **Multi-Provider Support** — Switching between Google Gemini, Hugging Face (cloud & local), and OpenAI with minimal code changes
- **Environment Management** — Securely loading API keys using `python-dotenv`

---

## 👤 Author

**Muhammad Ahmad Abbas**
- GitHub: [@r-muhammadahmadabbas](https://github.com/r-muhammadahmadabbas)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
