import streamlit as st
import openai
import os

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Chat với GPT-4o")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị toàn bộ hội thoại
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input("Bạn muốn hỏi gì?"):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o", messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assisstant", "content": reply})
