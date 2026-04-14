import streamlit as st
from rag_pipeline import generate_answer
from memory import add_to_memory

st.set_page_config(page_title="AI Chatbot")

st.title("🧠 AI Knowledge Base Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    response = generate_answer(user_input)

    st.session_state.messages.append(("bot", response))
    add_to_memory(user_input, response)

# Display chat
for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)