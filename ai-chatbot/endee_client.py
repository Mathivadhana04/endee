import json
import os
from embeddings import get_embedding
import numpy as np

# Simple local vector store (Endee-compatible approach)
DB_FILE = "vector_store.json"

# Load existing DB
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = []

def save_db():
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f)

def insert_document(text):
    vector = get_embedding(text)
    
    db.append({
        "text": text,
        "vector": vector
    })
    
    save_db()

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, top_k=3):
    query_vector = get_embedding(query)

    scored = []
    for item in db:
        score = cosine_similarity(query_vector, item["vector"])
        scored.append((score, item["text"]))

    scored.sort(reverse=True, key=lambda x: x[0])

    return scored[:top_k]   # return score + text