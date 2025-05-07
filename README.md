# 📊 Amazon 10-K RAG Assistant

A Retrieval-Augmented Generation (RAG) chatbot that answers questions grounded in Amazon’s official 10-K filings. Combines secure document indexing using AWS Bedrock with a Streamlit-based conversational UI to simulate a ChatGPT-like financial research assistant.

---

## 🔍 Overview

This project demonstrates the power of Retrieval-Augmented Generation for financial document analysis. Users can ask natural language questions (e.g., "What were Amazon's key risk factors in 2022?") and receive accurate, source-grounded answers directly from the 10-K filing.

---

## 🧠 Architecture

1. **Data Source**: Amazon’s 10-K filing (PDF or plain text)
2. **Indexing**: Content is embedded and indexed via AWS Bedrock Knowledge Base
3. **Retrieval**: Relevant chunks are retrieved based on semantic similarity to the user’s query
4. **Generation**: Claude / ChatGPT generates a grounded response using the retrieved context
5. **Frontend**: Streamlit interface mimicking a finance-focused chat assistant

---

## 🚀 Features

- 🔎 Semantic search over SEC filings
- 💬 Natural language Q&A interface
- 📂 RAG pipeline built with AWS Bedrock
- 🧱 Modular design for adapting to other public companies or filings

---

## 🛠️ Technologies Used

- Python 3.10+
- Streamlit
- AWS Bedrock (Knowledge Base, Claude)
- LangChain (optional)
- OpenAI / Anthropic APIs (fallback)
- PyPDF / txt parsing for SEC documents

---

## ⚙️ Setup Instructions

1. Clone this repository:
```bash
git clone https://github.com/deeko002/amazon-10k-rag-assistant.git
cd amazon-10k-rag-assistant
```
## ⚙️ Setup Instructions

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Set your credentials in .env or environment variables:
```bash
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
BEDROCK_REGION=
```
### Run the app:
```bash
streamlit run app.py
```

### 💡 Example Questions
- “Summarize Amazon’s financial highlights in 2022.”

- “What legal risks did Amazon disclose last year?”

- “How has AWS impacted Amazon’s revenue?”

### 📎 Future Improvements
- Add vector store fallback using FAISS or Pinecone

- Expand to multi-document (10-K + annual letters)

- Deploy on AWS Lambda + API Gateway for production use

### 📜 License
- This project is released under the MIT License.

### 👨‍💻 Author
- Tarun Kumar Deekonda
- MSBA Candidate @ UMN Carlson