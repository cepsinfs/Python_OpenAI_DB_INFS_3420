import streamlit as st
import openai
import mysecrets
import email_client

openai.api_key = mysecrets.openai_key



st.header("Sample Survey")

name = st.text_input("Full Name")
feedback = st.text_area("Please provide your feedback")
submit = st.button("Submit Survey")

if submit and name and feedback:
    response = openai.Completion.create(
        model = "text-davinci-003", 
        prompt = feedback, 
        max_tokens = 50,
        temperature = 0

    )
    reply = response['choices'][0]['text']

    email_client.send_response(reply, name)
    st.info("Thank you for your opinion, please check your inbox for our humble reponse")





else:
    st.warning("Please provide all information")


