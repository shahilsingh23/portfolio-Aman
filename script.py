import streamlit as st

# Hide the Streamlit interface with custom CSS
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Open and read the content of the index.html file
with open('index.html', 'r') as f:
    html_content = f.read()

# Display the HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)
