import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

n = st.number_input("Enter an integer", value = 1, step = 1)

squ = n ** 2
cube = n ** 3
fifth_power = n ** 5

st.write(f"The Square of {n} is: {squ}")
st.write(f"The Cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")