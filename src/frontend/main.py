import streamlit as st
import time
st.set_page_config(page_title="Chatbot with Groq & LangChain", layout="wide")
import pages.gvars
# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: black;
        }
        .stTextArea textarea {
            font-size: 18px !important;
            border: 3px solid white !important;
            border-radius: 10px !important;
            padding: 15px !important;
        }
        .stButton>button {
            background-color: white;
            color: black;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px 20px;
            border: 2px solid white;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #444;
            color: white;
            border: 2px solid white;
        }
        .stProgress > div > div > div > div {
            background: repeating-linear-gradient(
                -45deg,
                #ff4b4b,
                #ff4b4b 10px,
                #d63030 10px,
                #d63030 20px
            ) !important;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h2 style='text-align: center; color: white;'>Convert your ideas into reality</h2>", unsafe_allow_html=True)

# Input box
user_input = st.text_area("", placeholder="Type your prompt here...", height=100)

# Button
col1, col2, col3 = st.columns([3, 1, 3])
with col2:
    submit = st.button("➤")  # Unicode arrow for elegance

# Handle button click
if submit and user_input:
    st.success(f"Processing: {user_input}")
    # st.session_state["user_input"] = user_input
    pages.gvars.inp = user_input

    # Show progress bar when button is clicked
    progress_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.03)  # Adjust speed
        progress_bar.progress(percent)
    
    # Redirect or show success message after progress completes
    st.success("Done! Preparing SWOT analysis...")
    time.sleep(1)  # Pause briefly

    st.markdown('<meta http-equiv="refresh" content="0; URL=http://localhost:3000/task.html">', unsafe_allow_html=True)


# st.title("Welcome!")
# st.write("Select an option from the sidebar to proceed.")
