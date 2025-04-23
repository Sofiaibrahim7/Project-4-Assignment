import streamlit as st
import random

st.title("🎯 Guess the Number (Computer's Secret)")

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)

guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
if st.button("Guess"):
    if guess < st.session_state.number:
        st.warning("Too low!")
    elif guess > st.session_state.number:
        st.warning("Too high!")
    else:
        st.success("Correct! You guessed it!")
        st.session_state.number = random.randint(1, 100)
