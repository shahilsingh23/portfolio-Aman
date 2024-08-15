import streamlit as st

# Open and read the content of the index.html file
with open('index.html', 'r') as f:
    html_content = f.read()

# Display the HTML content in Streamlit
st.components.v1.html(html_content, height=600, scrolling=True)

# Optionally, add some Streamlit widgets or interactive elements
st.title("My Streamlit App")
st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
