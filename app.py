import streamlit as st
import random
import time

# Initialize session state variables
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if "button_position" not in st.session_state:
    st.session_state.button_position = {"top": 50, "left": 50}

# Title of the web app
st.title("💓 Love Message From Anot 💓")

# Introduction text
st.write(
    "Welcome to the Love Message From Anot 💓! Press the button below 22 times to see the special message 💓."
)

# Function to generate random button position
def random_position():
    return {"top": random.randint(0, 400), "left": random.randint(0, 400)}

# Update button position on click
def button_clicked():
    st.session_state.click_count += 1
    if st.session_state.click_count < 22:
        st.session_state.button_position = random_position()

# Container for the moving button
button_container = st.empty()

# Display button in a random position
position = st.session_state.button_position
button_style = f"""
    position: absolute;
    top: {position['top']}px;
    left: {position['left']}px;
    transform: translate(-50%, -50%);
"""
button_html = f"""
    <div style="{button_style}">
        <button onclick="fetch('/button_clicked')" style="padding: 10px; font-size: 16px;">Press Me Darlingg💓</button>
    </div>
"""

# Render the button
button_container.markdown(button_html, unsafe_allow_html=True)

# Check if the user has pressed the button 22 times
if st.session_state.click_count >= 22:
    # Show the love message after 22 clicks
    love_message = """
    I love you sayanggku, cintakuu, my lovee, my honey, my baby, my princess, 
    my darling, my favorite person, my sweet lovely special soft pink gummy bear, 
    my everything, my adventure, my one and only one, 
    yang paling aku sayanggg dan yang paling aku cintaa.
    """
    # Display the love message gradually, word by word with animation
    words = love_message.split()
    message_placeholder = st.empty()

    for i in range(len(words) + 1):
        message_placeholder.write(" ".join(words[:i]))
        time.sleep(0.3)
