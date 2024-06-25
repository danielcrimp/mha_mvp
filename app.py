import streamlit as st
import openai
from pydub import AudioSegment

# Initialize OpenAI API
# openai.api_key = st.secrets["openai_api_key"]
# # openai.api_key = Environment.OPENAI_API_KEY
#
# # Load Whisper model
# model = whisper.load_model("base")

st.title("MH Service")
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
