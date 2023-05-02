import streamlit as st
import pandas as pd
import dbcon
import mysql.connector
import analysis

st.header("Suvery Details")

mycursor, conn = dbcon.db()

qry = "select * from survey"

mycursor.execute(qry)

results = mycursor.fetchall()
students = []

for std in results:
    students.append(
        {
            "ID": std[0],
            "Feedback": std[1],
            "GPA": std[2], 
            "Year": std[3],
            "Name": std[4]

        }

    )
main_df = pd.DataFrame(students)
main_df['Polarity'] = main_df['Feedback'].apply(analysis.textPol)
main_df['Labels'] = main_df["Polarity"].apply(analysis.textAnalysis)

graph_vals = main_df.Labels.value_counts()
st.bar_chart(graph_vals)


unique_years = main_df['Year'].unique()

year = st.multiselect("Choose your Cohort", options=sorted(unique_years), default=sorted(unique_years))

with st.expander("Student Dataset"):
    st.write(main_df[main_df['Year'].isin(year)])

st.subheader("Cohort-wise Statistics")   
for cohort in year:
    with st.expander(f"{cohort} Statistics"):
        c1, c2, c3 = st.columns(3)
        sub = main_df[main_df['Year']==cohort]
        c1.metric("Maximum GPA", sub['GPA'].max())
        c2.metric("Minimum GPA", sub['GPA'].min())
        c3.metric("Average GPA", sub['GPA'].median())
        vals = sub.Labels.value_counts()
        st.bar_chart(vals)

        