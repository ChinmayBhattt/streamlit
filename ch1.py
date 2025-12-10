import streamlit as st

st.title("Hello World")
st.subheader("Made by Streamlit")
st.text("Welcome to the streamlit Playground")
st.write("Choose Your Fav Programing Lang.")

lang = st.selectbox("Your fav Programing Language: ", ["Python", "C++", "Javascript", "java"])
st.write(f"Your Choise {lang}. Exellent Choice")

st.success("done")