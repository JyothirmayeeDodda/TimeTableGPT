import streamlit as st

def returnTextboxInput():
    st.markdown("""
    <style>
    .title {
        text-align: center;
    }
    .input-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)
    st.title('GraduateTimetable GPT')
    inputprompt = st.text_input('Please enter the course code',value="",key="centered-input")
    
    return st,inputprompt

def returnSelection(st):
    option = st.selectbox('How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))
    return option
