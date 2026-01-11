from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv
import os
import uuid
from datetime import datetime

from pymongo import MongoClient
from langchain_community.llms import CTransformers
from langchain_core.prompts import PromptTemplate
from src.prompt import PROMPT  

# -----Flask app init------
app = Flask(__name__)
load_dotenv()

# -------------MongoDB setup----------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["Chat-Bot-db"]
chats = db["conversations"]

def save_message(session_id, role, content):
    """Save a single message to MongoDB in a session-based document."""
    chats.update_one(
        {"session_id": session_id},
        {
            "$push": {
                "messages": {
                    "role": role,
                    "content": content,
                    "timestamp": datetime.utcnow()
                }
            }
        },
        upsert=True
    )

# -----------------------------Load TinyLLaMA (CTransformers)---------------------------------------------
llm = CTransformers(
    model=r"A:\Classroom\PROJECTS\Medical-Chatbot_freecodecamp\model\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    model_type="llama",
    config={
        "max_new_tokens": 1200,      
        #"min_new_tokens": 400,       # not valid for pretrained models
        "temperature": 0.25,
        "top_p": 0.95,
        "top_k": 50,
        "repetition_penalty": 1.3,
        "context_length": 2048,
        "stop": ["\n\n\n"]           
    }
)

# --------------Routes---------------
@app.route("/")
def index():
    return render_template("main.html")  

# ----------------------Streaming chat route----------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    """Handles user message, generates LLM response, saves to MongoDB, streams reply."""
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data["message"]
    session_id = data.get("session_id", str(uuid.uuid4()))

    save_message(session_id, "user", user_message)

    prompt_text = PROMPT.format(context="", question=user_message)

    bot_reply = ""

    def generate():
        nonlocal bot_reply
        for token in llm.invoke(prompt_text, stream=True):
            bot_reply += token
            yield token  
        # After generation, save to MongoDB
        save_message(session_id, "assistant", bot_reply)

    # Use Response for streaming (if you later implement front-end token display)
    # For now, collect full reply and send as JSON
    full_reply = "".join(generate())
    return jsonify({"reply": full_reply, "session_id": session_id})

# -------------------Run the app------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
