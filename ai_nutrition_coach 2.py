import streamlit as st
import pandas as pd

# Title of the web app
st.title("AI-Powered Nutrition Coach")

# Add a description
st.write("Welcome to the AI-Powered Nutrition Coach! This app will help you track your diet and suggest healthy food options based on your preferences.")

# Ask the user for their name
name = st.text_input("Enter your name:")

# Ask the user for their age
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Ask for gender
gender = st.selectbox("Select your gender:", ("Male", "Female", "Other"))

# Ask for dietary preference
diet = st.selectbox("Select your dietary preference:", ("Vegetarian", "Non-Vegetarian", "Vegan"))

# Display the entered information
st.write(f"Hello {name}, you are a {age} year old {gender} with a {diet} diet.")

# Show suggestions based on age (you can customize this logic)
if age < 18:
    st.write("You are a young person, make sure to get enough nutrients like protein, calcium, and vitamins!")
elif 18 <= age <= 50:
    st.write("As an adult, focus on a balanced diet with healthy fats, proteins, and lots of vegetables.")
else:
    st.write("As a senior, ensure to focus on foods rich in fiber, calcium, and vitamin D.")

# Button for additional advice
if st.button("Get Nutrition Tips"):
    st.write("1. Drink plenty of water daily.")
    st.write("2. Avoid processed foods as much as possible.")
    st.write("3. Include fruits and vegetables in your daily meals.")
    st.write("4. Choose healthy snacks like nuts and seeds.")

# Add an image or illustration (optional)
st.image("https://upload.wikimedia.org/wikipedia/commons/4/46/Fruits_and_vegetables.jpg", caption="Healthy Foods")
import streamlit as st

# List of healthy foods
healthy_foods = ["Apple", "Banana", "Carrot", "Spinach"]

# Display the title for the section
st.markdown("### Healthy Foods")

# Display the list of healthy foods
st.write(healthy_foods)  # You can also use st.table(healthy_foods) to display as a table
