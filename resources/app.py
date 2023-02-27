import streamlit as st
import webbrowser

st.title("First Assignment Innomatics Research Labs")
st.header("Create Streamlit Data App")
st.subheader("shweta kulkarni")

linkedin = 'https://www.linkedin.com/in/shweta-kulkarni-ba8b53a9/'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)

github = 'https://github.com/SHWETADKULKARNI'

if st.button('GitHub'):
    webbrowser.open_new_tab(github)