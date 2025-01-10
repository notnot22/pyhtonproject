import streamlit as st

# Title of the web app
st.title("💓Love Message From Anot💓")

# Introduction text
st.write("Welcome to the Love Message From Anot! Press the button below to see the special message.")

# Button to trigger the display of the love message
if st.button("Press Me Gracee 💓💓"):
    love_message = """
    I love you sayanggku, cintakuu, my lovee, my honey, my baby, my princess, 
    my darling, my favorite person, my sweet lovely special soft pink gummy bear, 
    my everything, my adventure, my one and only one, 
    yang paling aku sayanggg dan yang paling aku cintaa.
    """
    
    # Display the love message after the button is pressed
    st.write(love_message)

    # Optionally display an image (e.g., a love-related image from a GitHub repository or URL)
    st.image("https://github.com/notnot22/pyhtonproject/blob/main/a7fb1871ef358d2508aef77f33541a1b.gif", caption="With Love")
