import streamlit as st
import openai
from pydub import AudioSegment

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("MH Service")

client = openai.OpenAI()

messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a therapist taking me through a mindfulness session. I may have had problems this week. Get me to talk through them and lead me to positivity."},
            {"role": "user", "content": prompt}
        ]
    )
    respon = completion.choices[0].message.content

    messages.chat_message("assistant").write(f"{respon}")