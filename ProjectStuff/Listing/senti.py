from textblob import TextBlob
import streamlit as st


txt = st.text_input("Say Something")

if(txt):
    subScore = TextBlob(txt).sentiment.subjectivity
    polScore = TextBlob(txt).sentiment.polarity

    st.write(f"Subjectivity of the statment is: {subScore}")
    st.write(f"Polarity of the statment is: {polScore}")

    if(polScore>0):
        st.write("Its a positive Feedback")

    elif(polScore == 0):
        st.write("Its neutral")

    elif(polScore<0):
        st.write("Customer is not happy")