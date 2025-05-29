
import json
import streamlit as st

with open("marketing_faq.json", "r") as f:
    faq = json.load(f)

def answer_question(question):
    for key in faq:
        if question.lower() in key.lower():
            return faq[key]
    return "Sorry, I don't know the answer to that. Try asking something else!"

st.title("Marketing AI Tutor")
question = st.text_input("Ask a marketing question:")
if question:
    st.write("Answer:", answer_question(question))
