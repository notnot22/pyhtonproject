import streamlit as st
import time

# Initialize click counter in session state
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# Title of the web app
st.title("💕 Love Message From Anot 💕")

# Introduction text
st.write("Welcome to the Love Message From Anot 💕! Find and press the button below 22 times to see the special message 💕.")

# Add heart rain animation to the page
heart_rain_html = """
    <style>
        .heart {
            position: absolute;
            top: -50px;
            font-size: 30px;
            animation: fall 5s linear infinite;
        }

        @keyframes fall {
            0% {
                top: -50px;
                opacity: 1;
            }
            100% {
                top: 100vh;
                opacity: 0;
            }
        }

        .heart:nth-child(odd) {
            left: calc(100% * var(--x-pos, 0) - 50px);
            animation-duration: calc(5s + var(--speed, 0s));
            animation-delay: calc(var(--delay, 0s) * -1);
        }

        .heart:nth-child(even) {
            left: calc(100% * var(--x-pos, 0) - 50px);
            animation-duration: calc(5s + var(--speed, 0s));
            animation-delay: calc(var(--delay, 0s) * -1);
        }
    </style>
    <script>
        const heartsContainer = document.createElement('div');
        document.body.appendChild(heartsContainer);

        function generateHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.textContent = '💖';
            heartsContainer.appendChild(heart);

            heart.style.setProperty('--x-pos', Math.random());
            heart.style.setProperty('--speed', Math.random() * 2 + 's');
            heart.style.setProperty('--delay', Math.random() * 3 + 's');
        }

        setInterval(generateHeart, 300);
    </script>
"""

st.markdown(heart_rain_html, unsafe_allow_html=True)

# Add moving button with JavaScript
button_html = f"""
    <script>
        function moveButton() {{
            const button = document.getElementById('moving-button');
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 50);
            button.style.position = 'absolute';
            button.style.left = `${{x}}px`;
            button.style.top = `${{y}}px`;
        }}

        document.getElementById('moving-button').addEventListener('click', () => {{
            moveButton();
            fetch('/button_clicked');
        }});
    </script>
    <button id="moving-button" onclick="moveButton()">Press Me Darlingg❤️</button>
"""

# Track clicks in Python
if st.button("Button Clicked"):
    st.session_state.click_count += 1

    if st.session_state.click_count >= 22:
        # Show the love message after 22 clicks
        love_message = """
        I love you sayanggku, cintakuu, my lovee, my honey, my baby, my princess, 
        my darling, my favorite person, my sweet lovely special soft pink gummy bear, 
        my everything, my adventure, my one and only one, 
        yang paling aku sayanggg dan yang paling aku cintaa beneran.
        """
        # Display the love message gradually, word by word with animation
        words = love_message.split()
        message_placeholder = st.empty()

        for i in range(len(words) + 1):
            message_placeholder.write(" ".join(words[:i]))
            time.sleep(0.3)

st.image("https://github.com/notnot22/pyhtonproject/blob/main/a7fb1871ef358d2508aef77f33541a1b.gif", caption="With Love Anot")

