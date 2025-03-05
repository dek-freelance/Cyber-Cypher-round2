import streamlit as st
import requests
import PyPDF2
import json
import pages.gvars

st.set_page_config(page_title="PDF Summarizer", layout="centered")

# Hide Streamlit's default menu
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("PDF Summarizer with Chat")

# Define roles
RolesNum = {
    "11": "DOCUMENT_SUMMARIZER"
}
selected_role_key = st.selectbox("Select a Task Role:", list(RolesNum.values()))
selected_role = selected_role_key

# Get role key
keyArray = [key for key, val in RolesNum.items() if val == selected_role]
roleVariable = keyArray[0]

# File uploader
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = "".join([page.extract_text() or "" for page in pdf_reader.pages])
    return text

pdf_text = ""
if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text", pdf_text[:1000] + "..." if len(pdf_text) > 1000 else pdf_text, height=200)

# Chat interface
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

    url = 'http://localhost:8001/api/v1/chatgroq'
    myobj = {'role': roleVariable, 'msg': pages.gvars.inp + ", " + user_input}
    response = requests.post(url, json = myobj)
    response = response.json()[0].strip('["]')

    print("here", type(response[0]))
    st.session_state.messages.append({"role": "assistant", "content":  response})
    
    with st.chat_message("assistant"):
        st.markdown(response)
