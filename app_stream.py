import streamlit as st
from src.backend.groq_chat import req_groq_langchain
from src.config.constants import Roles

st.set_page_config(page_title="Chatbot with Groq & LangChain", layout="centered")

st.title("BhashaBridge AI Assistance")


# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from Groq
    response = req_groq_langchain(Roles.IDEATION_STRATEGIC_ROADMAP_GENERATOR, user_input)

    st.session_state.messages.append({"role": "assistant", "content": response["text"]})
    
    with st.chat_message("assistant"):
        st.markdown(response)
