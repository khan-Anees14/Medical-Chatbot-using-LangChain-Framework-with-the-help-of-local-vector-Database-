🩺 Medical Chatbot using Local LLM (Flask + LangChain)

A medical question–answering chatbot built using Flask, LangChain, and a local Large Language Model (LLM).
The chatbot provides token-by-token streaming responses, supports dark mode, and has a modern chat UI similar to ChatGPT.

⚠️ This chatbot is for educational and informational purposes only and does not replace professional medical advice.

🚀 Features

🧠 Local LLM (No OpenAI API required)

🔎 Retrieval-Augmented Generation (RAG) using FAISS

💬 Token-by-token streaming UI (live typing effect)

🌙 Dark Mode toggle

🎨 Clean ChatGPT-style UI

🗂️ Medical document embeddings (HuggingFace)

🧑‍⚕️ Medical-focused responses

⚡ Lightweight & beginner-friendly

🛠️ Tech Stack

Frontend  -> HTML, CSS, JavaScript

Backend	-> Flask

Mongo-DB  ->   for storing Chat between user and Bot

LLM Framework	-> LangChain

Embeddings	-> HuggingFace

Vector DB	-> FAISS

Local Model	-> TinyLLaMA / LLaMA (GGUF)

Styling	    -> Custom CSS (Light + Dark mode)


💬 How It Works

User enters a medical query

Query is embedded using HuggingFace embeddings

Relevant medical documents retrieved via FAISS

Prompt sent to local LLM

Response streamed token-by-token to UI

🌙 Dark Mode

Click Dark Mode in the sidebar to toggle between:

☀️ Light Mode

🌙 Dark Mode

⚠️ Medical Disclaimer

This chatbot is not a doctor.
It provides general medical information only.
Always consult a qualified healthcare professional for diagnosis and treatment.


🔮 Future Improvements

✅ True backend streaming (WebSockets)

🧠 Conversation memory

📄 PDF upload support

📱 Mobile responsiveness

☁️ Cloud deployment

🧪 Model fine-tuning



👤 Author

Mohmmad Anish
M.SC. AI & ML | GenAI Project
