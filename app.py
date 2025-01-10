import streamlit as st
import time

# Title of the web app
st.title("Love Message App")

# Introduction text
st.write("Welcome to the Love Message app! Press the button below to see the special message.")

# Button to trigger the display of the love message
if st.button("Tekan Aku"):
    love_message = """
    I love you sayanggku, cintakuu, my lovee, my honey, my baby, my princess, 
    my darling, my favorite person, my sweet lovely special soft pink gummy bear, 
    my everything, my adventure, my one and only one, 
    yang paling aku sayanggg dan yang paling aku cintaa.
    """
    
    # Display the love message gradually, word by word with animation
    words = love_message.split()
    message_placeholder = st.empty()  # Placeholder for dynamic content
    
    for i in range(len(words) + 1):
        # Update the placeholder with increasing words
        message_placeholder.write(" ".join(words[:i]))
        time.sleep(0.3)  # Delay between word reveals

    # Optionally display an image after message
    st.image("https://github.com/your-username/your-repo/raw/main/love_image.jpg", caption="With Love")
