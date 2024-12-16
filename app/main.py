import streamlit as st
from utils import test_internet_speed
from styles import HEADER_STYLE, RESULT_BOX_STYLE
import logging

# Configure logging
logging.basicConfig(
    filename="logs/internet_speed.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    st.set_page_config(page_title="Internet Speed Checker", layout="centered")

    # App Header
    st.markdown(HEADER_STYLE, unsafe_allow_html=True)

    # Instruction
    st.markdown(
        "<h4 style='text-align: center; color: #FF5722;'>Click the button below to check your internet speed.</h4>",
        unsafe_allow_html=True
    )

    if st.button("Test Internet Speed"):
        with st.spinner("Testing your internet speed. Please wait..."):
            download_speed, upload_speed, ping = test_internet_speed()

        if download_speed and upload_speed:
            st.success("Internet speed test completed successfully!")
            st.markdown(
                RESULT_BOX_STYLE.format(
                    download_speed=download_speed,
                    upload_speed=upload_speed,
                    ping=ping
                ),
                unsafe_allow_html=True
            )
        else:
            st.error("Failed to test internet speed. Check your connection and try again.")

    st.sidebar.header("About")
    st.sidebar.info(
        """
        This app measures your:
        - Download speed
        - Upload speed
        - Ping
        
        Built with ❤️ using Streamlit.
        """
    )

if __name__ == "__main__":
    main()
