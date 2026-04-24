# 🤖 GenAI Sprint Lab 
---

## 🛠️ Tech Stack

- **Google Gemini API** — free LLM API
- **Hugging Face Transformers** — local models (GPT-2, BERT, distilBART)
- **Sentence Transformers** — embeddings for RAG
- **PyTorch** — GAN implementation
- **FAISS** — vector search
- **Google Colab** — free GPU environment

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install google-generativeai transformers sentence-transformers faiss-cpu torch torchvision
```

### 2. Get a free API key
Go to → [https://aistudio.google.com](https://aistudio.google.com) and create a free API key.

### 3. Add your key in the notebook
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")
```
---

## 🎯 Final Project — Text Analysis Tool

Combines three tools into one pipeline:

- **Token Counter** — counts tokens using BERT tokenizer
- **Summarizer** — generates a concise summary via Gemini
- **Report** — prints a clean combined analysis output

```python
# Sample output
====== TEXT ANALYSIS REPORT ======
Original Text : Artificial Intelligence is transforming the world...
Token Count   : 38
Summary       : AI is revolutionizing industries worldwide...
==================================
```

---

## ✅ Deliverables

- [x] Notebook completed
- [x] Tokenization outputs (BERT vs GPT-2)
- [x] Summarization working
- [x] Chatbot with conversation history
- [x] RAG pipeline working
- [x] GAN Generator & Discriminator implemented
- [x] Final Text Analysis Tool complete

---

## 💡 Key Learnings

- Prompt quality directly controls output quality
- RAG solves the LLM memory problem using embeddings + vector search
- GANs use a Generator vs Discriminator adversarial game (Ian Goodfellow, 2014)
- Gemini outperforms local HuggingFace models for most tasks
- `gemini-2.5-flash` is the best free-tier model for this course

---

## 📜 License
This project is for educational purposes only.
