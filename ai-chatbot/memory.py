chat_memory = []

def add_to_memory(user, bot):
    chat_memory.append({
        "user": user,
        "bot": bot
    })

def get_memory():
    return chat_memory[-5:]