import streamlit as st

st.title("Test Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/11388725/pexels-photo-11388725.jpeg", width=100)
    vote1 = st.button("Vote Masala Chain")

with col2:
    st.header("Addharak Chai")
    st.image("https://images.pexels.com/photos/34924729/pexels-photo-34924729.jpeg", width=85)
    vote2 = st.button("Vote Addharak Chain")


if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adhrak chai ")

name = st.sidebar.text_input("Enter Your Name: ")
tea = st.sidebar.selectbox("Choose Your Chai ", ["Masala", "Kesar", "Adhark"])
st.write(f"Welcome {name} and your {tea} chain is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write(""" 
    1. Boil water with tea leaves
    2. Add milk and Spices
    3. Serve hot
""")
    
st.markdown('### Welcome To Chai App')
st.markdown('> Blockquote ')