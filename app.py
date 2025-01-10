# app.py

import streamlit as st

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Message of Love",
    page_icon="❤️",
    layout="centered"
)

# Style for centering content
st.markdown(
    """
    <style>
    .center-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
    }
    .button {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown(
    """
    <div class="center-content">
        <h1>❤️ A Special Button ❤️</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Add a button and show centered message
if st.button("Tekan Aku", key="unique_button", help="Klik untuk melihat pesan dari anot"):
    st.markdown(
        """
        <div class="mark">
    """,
