import streamlit as st
from openai import OpenAI
from pydub import AudioSegment
from dotenv import  load_dotenv

load_dotenv()

st.title("MH Service")


client = OpenAI()

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


#
# # Audio input
# audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])
#
# if audio_file:
#     # Convert to a format Whisper can read
#     audio = AudioSegment.from_file(audio_file)
#     audio.export("temp.wav", format="wav")
#
#     # Process audio file with Whisper
#     transcription = model.transcribe("temp.wav")["text"]
#     st.write("Transcription:", transcription)
#
#     # Process transcription with GPT-4
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=transcription,
#         max_tokens=150
#     )
#     st.write("GPT-4 Response:", response.choices[0].text)
#
#     # Cleanup
#     import os
#     os.remove("temp.wav")
