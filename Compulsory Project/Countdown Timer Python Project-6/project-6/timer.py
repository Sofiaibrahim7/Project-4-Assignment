import streamlit as st
import time

st.title("⏳ Countdown Timer")

seconds = st.number_input("Enter countdown time in seconds:", min_value=1, step=1)

if st.button("Start"):
    st.write("Timer started...")
    progress = st.empty()
    for i in range(seconds, 0, -1):
        progress.markdown(f"# ⏰ {i} seconds remaining")
        time.sleep(1)
    st.success("⏱ Time's up!")
