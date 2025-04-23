import streamlit as st

st.title("💻 Let Computer Guess Your Number")

if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 100
if 'guess' not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

st.write(f"My guess is: **{st.session_state.guess}**")

feedback = st.radio("Is the guess:", ["Too Low", "Too High", "Correct"])

if st.button("Submit Feedback"):
    if feedback == "Too Low":
        st.session_state.low = st.session_state.guess + 1
    elif feedback == "Too High":
        st.session_state.high = st.session_state.guess - 1
    elif feedback == "Correct":
        st.success("Yay! I guessed it!")
        st.session_state.low = 1
        st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
