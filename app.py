import os
import sys
import streamlit as st
import streamlit.web.cli as stcli

def main():
    st.title("Hello Tracy!")
    st.write("Your Streamlit environment is working 🎉")

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        "app.py",
        "--server.port",
        os.environ.get("PORT", "8000"),
        "--server.address",
        "0.0.0.0"
    ]
    # Start Streamlit
    main()
    sys.exit(stcli.main())
