import openai
import streamlit as st

openai.api_key = st.secrets["KEY"]["API_KEY"]


def generate_response(prompt):
    completion = openai.Completion.create(engine="gpt-3.5-turbo",
                                          prompt=prompt,
                                          max_tokens=1024,
                                          temperature=0.3) 
    message = completion.choices[0].text 
    return message 

st.title("""
         GPTAI HOPT Focasting diseases
         """)

def get_text():
    input_text = st.text_input("HOPT: ",)
    return input_text 

user_input = get_text()

if user_input:
    st.text_area("GPTAI", value=generate_response(user_input), height=600, max_chars=None)
else:
    st.text_area("GPTAI", value="Mời bạn cho thông tin cần tìm", height=600, max_chars=None)