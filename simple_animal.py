# save this as simple_app.py and run with: streamlit run simple_app.py

import streamlit as st

st.title("🐾 Favorite Animal Survey")

# User input
name = st.text_input("What is your name?")
animal = st.selectbox("Pick your favorite animal:", ["Dog", "Cat", "Rabbit", "Elephant", "Penguin"])

# Optional slider
rating = st.slider("How much do you love this animal?", 0, 10, 5)

# Submit button
if st.button("Submit"):
    st.write(f"Hi {name}! You chose **{animal}**, and your love rating is {rating}/10. 🧡")
    if animal == "Dog":
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golde33443.jpg/800px-Golde33443.jpg", caption="Good boy!")
    elif animal == "Cat":
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg", caption="What a cat!")
    elif animal == "Rabbit":
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/3b/Oryctolagus_cuniculus_Tasmania.jpg", caption="Bunny!")
    elif animal == "Elephant":
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg", caption="Big love!")
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/fb/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juveniles-8.jpg", caption="Cool penguin!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
