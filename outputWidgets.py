
def outputToScreen(st,response):
    st.markdown("""
    <style>
    .title {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(response,unsafe_allow_html=True)