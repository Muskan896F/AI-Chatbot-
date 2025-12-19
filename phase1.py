import streamlit as st

st.title("RAG Chatbot")

prompt = st.chat_input("Pass your prompt here!")

if prompt:
    st.chat_message("user").markdown(prompt)
    