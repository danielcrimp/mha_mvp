import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("MH Service")

client = openai.OpenAI()

if "disp_messages" not in st.session_state:
    st.session_state.disp_messages = []
if "message_list" not in st.session_state:
    st.session_state.message_list = [
        {"role": "system", "content": "You are a therapist taking me through a mindfulness session. I may have had problems this week. Get me to talk through them and lead me to positivity."},
    ]

for msg in st.session_state.disp_messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

if prompt := st.chat_input("Say something"):
    st.chat_message("user").write(prompt)
    st.session_state.disp_messages.append({"role": "user", "content": prompt})
    st.session_state.message_list.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.message_list
    )
    
    respon = completion.choices[0].message.content

    st.chat_message("assistant").write(respon)
    st.session_state.disp_messages.append({"role": "assistant", "content": respon})
    st.session_state.message_list.append({"role": "assistant", "content": respon})


