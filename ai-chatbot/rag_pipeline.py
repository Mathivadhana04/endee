from endee_client import search

def generate_answer(query):
    results = search(query)

    if not results:
        return "I don’t have information about this in my knowledge base."

    best_score, best_doc = results[0]

    # Threshold check (IMPORTANT)
    if best_score < 0.5:
        return "I don’t have information about this in my knowledge base."

    return best_doc