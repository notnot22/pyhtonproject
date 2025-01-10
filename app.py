import streamlit as st
import time

# Title of the web app
st.title("Love Message App")

# Introduction text
st.write("Welcome to the Love Message app! Press the button below to see the special message.")

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

        /* Randomize heart's position */
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
        // Generate hearts at random positions
        const heartsContainer = document.createElement('div');
        document.body.appendChild(heartsContainer);

        function generateHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.textContent = '💖';
            heartsContainer.appendChild(heart);

            // Random position and animation timing
            heart.style.setProperty('--x-pos', Math.random());
            heart.style.setProperty('--speed', Math.random() * 2 + 's');
            heart.style.setProperty('--delay', Math.random() * 3 + 's');
        }

        // Generate hearts continuously
        setInterval(generateHeart, 300);
    </script>
"""

# Add the heart rain animation to the Streamlit page using markdown (with unsafe_allow_html)
st.markdown(heart_rain_html, unsafe_allow_html=True)

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

    # Optionally display an image after the message
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fmymelody-love-sticker-mymelody-love-hearts-discover-share-gifs--592997475953385044%2F&psig=AOvVaw1X9N9UQXmgLBJJEM9xpb6B&ust=1736576690270000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMCqrrrC6ooDFQAAAAAdAAAAABAI", caption="With Love")
