# app.py

import streamlit as st

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Message of Love",
    page_icon="❤️",
    layout="centered"
)

# CSS for flying hearts animation
st.markdown(
    """
    <style>
    body {
        margin: 0;
        overflow: hidden;
    }
    .center-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
    }
    .hearts {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: -1;
    }
    .heart {
        position: absolute;
        width: 20px;
        height: 20px;
        background: red;
        opacity: 0.7;
        transform: rotate(45deg);
        animation: fly 4s linear infinite;
    }
    .heart:before, .heart:after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        background: red;
        border-radius: 50%;
    }
    .heart:before {
        top: -10px;
        left: 0;
    }
    .heart:after {
        top: 0;
        left: -10px;
    }
    @keyframes fly {
        0% {
            transform: translateY(100vh) rotate(45deg);
            opacity: 1;
        }
        100% {
            transform: translateY(-10vh) rotate(45deg);
            opacity: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML for flying hearts
hearts_html = """
<div class="hearts">
    {hearts}
</div>
""".format(
    hearts="\n".join(
        [
            f'<div class="heart" style="left: {i * 10}%; animation-delay: {i * 0.2}s;"></div>'
            for i in range(10)
        ]
    )
)

# Display the main title
st.markdown(
    """
    <div class="center-content">
        <h1>❤️ A Special Button ❤️</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Button to reveal the flying hearts animation
if st.button("Tekan Aku"):
    st.markdown(
        f"""
        <div class="center-content">
            <h2>I love you forever and ever, my love, with all my heart. ❤️</h2>
        </div>
        {hearts_html}
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div class="center-content">
            <p>Tekan tombol di atas untuk melihat pesan dari Anot! ❤️</p>
        </div>
        """,
        unsafe_allow_html=True
    )
