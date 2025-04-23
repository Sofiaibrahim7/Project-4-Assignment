import streamlit as st

st.title("⚖️ BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (m):", min_value=0.1)

if weight and height:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")
    if bmi < 18.5:
        st.info("Underweight")
    elif bmi < 24.9:
        st.success("Normal weight")
    elif bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obese")
