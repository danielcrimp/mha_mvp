import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Buddy - Pocket Therapist")

client = openai.OpenAI()

if "disp_messages" not in st.session_state:
    st.session_state.disp_messages = []
if "message_list" not in st.session_state:
    st.session_state.message_list = [
        {"role": "system", "content": "You are a therapist taking me through a mindfulness session. I may have had problems this week. Get me to talk through them and lead me to positivity." \
                                      "prioritise asking questions, don't produce answers more than a couple of sentences. You should feel completely comfortable sending a message of a couple of words. It should be conversational. Avoid massive screeds of advice and bullet points." \
                                      "Also, cut to the chase. If you want to get to a point, don't worry about going via multiple questions." \
                                      "Also, if the topic of self harm comes up from the user, please report the following message or a scenario specific variant of it:" \
                                      "Hey, some of the information you've shared has me a bit concerned. Please consider getting in contact with support. If you or someone you know is in immediate danger, please call 999 without delay. For mental health support, there are UK helplines and support services available 24/7, such as Samaritans at 116 123 and Mind at 0300 123 3393. Your well-being is important, and there are professionals ready to assist you."}
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
        model="gpt-4o",
        messages=st.session_state.message_list
    )
    
    respon = completion.choices[0].message.content

    st.chat_message("assistant").write(respon)
    st.session_state.disp_messages.append({"role": "assistant", "content": respon})
    st.session_state.message_list.append({"role": "assistant", "content": respon})


