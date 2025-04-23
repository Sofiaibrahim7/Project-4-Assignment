import streamlit as st
import random

words = ['python', 'streamlit', 'hangman', 'code']
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.display = ['_'] * len(st.session_state.word)
    st.session_state.lives = 6
    st.session_state.guessed = []

st.title("🪓 Hangman Game")

guess = st.text_input("Enter a letter:")

if st.button("Guess"):
    if guess in st.session_state.guessed:
        st.warning("Already guessed!")
    elif guess in st.session_state.word:
        for i, l in enumerate(st.session_state.word):
            if l == guess:
                st.session_state.display[i] = guess
    else:
        st.session_state.lives -= 1
    st.session_state.guessed.append(guess)

st.write("Word: " + " ".join(st.session_state.display))
st.write(f"Lives left: {st.session_state.lives}")

if "_" not in st.session_state.display:
    st.success("🎉 You won!")
elif st.session_state.lives == 0:
    st.error(f"Game Over! The word was {st.session_state.word}")
