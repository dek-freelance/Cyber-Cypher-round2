import streamlit as st
import time

st.set_page_config(page_title="Chatbot with Groq & LangChain", layout="centered")

# Custom CSS for improved styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stButton>button {
            background-color: #1DB954;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 30px;
            padding: 15px 30px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #17a34a;
            transform: scale(1.1);
        }
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #ff4b4b, #d63030);
            border-radius: 10px;
        }
        h1 {
            font-size: 36px !important;
            margin-bottom: 15px;
        }
        p {
            font-size: 20px !important;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with better typography and spacing
st.markdown("""
    <h1 style='text-align: center; font-size: 36px; color: white; font-weight: bold;'>
        🌉 Welcome to BhashaBridge
    </h1>
    <p style='text-align: center; font-size: 20px; color: #aaa;'>
        Your AI-powered language assistant
    </p>
    """, unsafe_allow_html=True)

# Centered Button
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    submit = st.button("➤ Start", key="start_button")

# Handle button click
if submit:
    st.success("Processing your request...")
    progress_bar = st.progress(0)
    
    for percent in range(101):
        time.sleep(0.02)
        progress_bar.progress(percent)
    
    st.success("Done! Redirecting...")
    time.sleep(1)
    
    st.markdown('<meta http-equiv="refresh" content="0; URL=http://localhost:3000/task.html">', unsafe_allow_html=True)
