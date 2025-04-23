import streamlit as st
import random

st.title("✊🖐✌ Rock, Paper, Scissors")

options = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Choose one:", options)
computer_choice = random.choice(options)

if st.button("Play"):
    st.write(f"Computer chose: **{computer_choice}**")
    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        st.success("You win!")
    else:
        st.error("You lose!")
