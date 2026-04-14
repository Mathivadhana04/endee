from endee_client import search
from memory import get_memory

def generate_answer(query):
    docs = search(query)
    context = "\n".join(docs)

    memory = get_memory()
    memory_text = "\n".join(
        [f"User: {m['user']}\nBot: {m['bot']}" for m in memory]
    )

    # Simple AI logic (no OpenAI needed for now)
    answer = f"""
Based on the knowledge base:

{context}

Previous conversation:
{memory_text}

Answer:
{context.split('.')[0]}
"""

    return answer