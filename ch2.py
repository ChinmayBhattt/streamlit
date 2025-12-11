import streamlit as st

st.title("Chai Maker App")


list = ["Milk","Chai Patti","Sugar","Water","ilaichi","adhrak"]

for item in list:
    st.checkbox(item)


# if item:
#     st.write("Masala added to your chain")

tea_type = st.radio("Pick Your Chai Type: ", ["Masala","Kesar Chai","Hot Tea","Black Tea"])
st.write(f"Selected Base {tea_type}")

flavour = st.selectbox("Choose Flavour: ", ["Adhrak","Kesar","Tulsi"])

st.write(f"Selected Flavour {flavour}")

sugar = st.slider("Sugar Level", 0,5,2)
st.write(f"Sugar spoon {sugar}")

cups = st.number_input("How Many Cups", min_value=1, max_value=10, step=1)
st.write(f"Cups spoon {cups}")


name = st.text_input("Enter Your Name: ")

if name:
    st.write(f"Welcome, {name} Your Chai is on the way")


dob = st.date_input("Select your Data of Birth")
st.write(f"Your Data of Birth is {dob}")


if st.button("Make Chain"):
    st.success("Your Chai is Ready")



