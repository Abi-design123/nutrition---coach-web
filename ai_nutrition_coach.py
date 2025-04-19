import streamlit as st

# Simple nutrition coach app
st.title("AI Nutrition Coach")
st.write("Welcome to the AI-powered Nutrition Coach!")

# User input for food item
food_item = st.text_input("Enter the food item you ate:")

if food_item:
    st.write(f"You entered: {food_item}")
    
    # Here you can integrate your AI model or logic to suggest nutrition info
    # For now, let's simulate a simple response
    nutrition_info = {
        "apple": "Calories: 52 kcal, Carbs: 14g, Protein: 0.3g, Fat: 0.2g",
        "banana": "Calories: 89 kcal, Carbs: 23g, Protein: 1.1g, Fat: 0.3g",
        "carrot": "Calories: 41 kcal, Carbs: 10g, Protein: 0.9g, Fat: 0.2g"
    }
    
    # If the food item is recognized, show nutrition info
    if food_item.lower() in nutrition_info:
        st.write(f"Nutrition Info: {nutrition_info[food_item.lower()]}")
    else:
        st.write("Sorry, I don't have nutrition info for that food yet.")
else:
    st.write("Please enter a food item to get nutrition information.")
