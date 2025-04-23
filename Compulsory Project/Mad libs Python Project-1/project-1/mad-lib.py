import streamlit as st

st.title("📝 Mad Libs Game")

adj1 = st.text_input("Enter an adjective:")
animal = st.text_input("Enter an animal:")
name = st.text_input("Enter a name:")
verb1 = st.text_input("Enter a verb:")
adj2 = st.text_input("Enter another adjective:")
person = st.text_input("Enter a person's name:")
verb2 = st.text_input("Enter another verb:")

if st.button("Generate Story"):
    story = f"""Once upon a time, there was a {adj1} {animal} named {name}.
This {animal} loved to {verb1} every day. One day, it met a {adj2} {person}
who helped it to {verb2} better. And they lived happily ever after."""
    st.success("Your Story:")
    st.write(story)
