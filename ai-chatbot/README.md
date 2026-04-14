# 🧠 AI Knowledge Base Chatbot with Memory using Endee

---

## 📌 Project Overview

This project is an AI-powered chatbot that uses a vector database approach (Endee) to store and retrieve knowledge. It implements **Retrieval-Augmented Generation (RAG)** along with **conversation memory** to provide context-aware and meaningful responses.

Unlike traditional chatbots, this system:

* Retrieves relevant information from stored data
* Remembers previous interactions
* Generates better, context-aware answers

---

## 🎯 Objectives

* Build a chatbot using **RAG (Retrieval-Augmented Generation)**
* Implement **semantic search** using embeddings
* Store and retrieve knowledge using a vector database approach
* Add **memory (Agentic AI behavior)** for better conversations

---

## 🚀 Features

* 🔍 Semantic Search (meaning-based search, not keyword-based)
* 🧠 Retrieval-Augmented Generation (RAG)
* 💬 Conversation Memory (remembers last interactions)
* ⚡ Fast retrieval using vector similarity
* 🌐 Interactive UI using Streamlit

---

## 🏗️ System Architecture

User Input
→ Embedding Generation
→ Vector Storage (Endee concept)
→ Similarity Search
→ Retrieve Relevant Data
→ Generate Response with Memory
→ Display Output

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **Sentence Transformers** (Embeddings)
* **NumPy** (Vector similarity)
* **Endee** (Vector DB concept)

---

## 📂 Project Structure

```
ai-chatbot/
│
├── app.py                # Streamlit UI
├── embeddings.py        # Embedding generation
├── endee_client.py      # Vector storage & retrieval
├── rag_pipeline.py      # RAG logic
├── memory.py            # Chat memory
├── load_data.py         # Load dataset into vector store
├── data/
│   └── sample_docs.txt  # Dataset
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone Repository

```
git clone https://github.com/Mathivadhana04/endee.git
cd endee/ai-chatbot
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Load Dataset

```
python load_data.py
```

---

### 4. Run Application

```
python -m streamlit run app.py
```

---

## 💡 Example Queries

* What is Artificial Intelligence?
* Explain Machine Learning
* What is Streamlit?
* What is a vector database?

---

## 🧠 How It Works

1. User enters a query
2. Query is converted into embeddings
3. Similar vectors are retrieved from stored data
4. Relevant context is selected
5. Previous conversation memory is added
6. Final response is generated and shown

---

## 📊 Key Concepts Used

* Semantic Search
* Vector Embeddings
* Cosine Similarity
* Retrieval-Augmented Generation (RAG)
* Agentic Memory

---

## 👩‍💻 Author

**Mathivadhana P**

---

## ✅ Conclusion

This project demonstrates how modern AI systems combine:

* Vector databases
* Retrieval mechanisms
* Memory systems

to build intelligent, context-aware applications.

## 📸 Screenshots

### Chat Interface
![Chat UI](assets/screenshot1.png)

### Example Output
![Output](assets/screenshot2.png)

---
