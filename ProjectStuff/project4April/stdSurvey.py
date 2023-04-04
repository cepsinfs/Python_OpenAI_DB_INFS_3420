import streamlit as st
from streamlit_option_menu import option_menu

import addSurvey

#pip install streamlit-option-menu

st.title("Student Exit Survey")

# Create the main menu

with st.sidebar:
    menu = option_menu("Main menu", 
            options=["Participate","Search", "Email"], 
            menu_icon="house", 
            icons=['chat-left','binoculars', 'envelope' ])

if menu == "Participate":
    addSurvey.survey()

if menu == "Email":
    pass

if menu == "Search":
    pass
