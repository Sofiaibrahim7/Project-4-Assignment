import streamlit as st
import random
import string

st.title("🔐 Password Generator")

length = st.slider("Select password length:", 4, 32)

if st.button("Generate Password"):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    st.code(password)
