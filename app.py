# app.py

import streamlit as st

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Message of Love",
    page_icon="❤️",
    layout="centered"
)

# Display the title
st.title("❤️ A Special Button ❤️")

# Add a button to reveal the message
if st.button("Tekan Aku"):
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; color: #FF4081;">
            I love you forever and ever,<br>
            my love,<br>
            with all my heart.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add a decorative footer
    st.markdown(
        """
        <hr>
        <div style="text-align: center; color: #6A1B9A; font-size: 16px;">
            💕 From the depths of my soul 💕
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Tekan tombol di atas untuk melihat pesan dari anot! ❤️")
