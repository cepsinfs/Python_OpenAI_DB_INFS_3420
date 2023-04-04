# file/form for survey submission
import streamlit as st
import dblink

dbcursor, conn = dblink.dbconnect()

def survey():
    st.header("Please share your experience here")

    col1, col2 = st.columns(2)

    name = col1.text_input("Full Name")
    cohort = col2.selectbox("Choose your cohort", options=range(2018, 2023))
    feedback = st.text_area("Your Feedback")
    submit = st.button("Submit Your Survery")

    if submit:
        if name and cohort and feedback:
            #insert data to the DV
            vals = (name, cohort, feedback)
            qry = "insert into information (name, cohort, feedback) values (%s, %s, %s)"
            dbcursor.execute(qry, vals)
            conn.commit()
            st.success("Thank you for sharing your opinion with us")




        else:
            st.error("Please fill in all information ")

