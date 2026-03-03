import streamlit as st

st.title("Hello Tracy!")
st.write("Your Streamlit environment is working 🎉")

import os
import streamlit.web.cli as stcli
import sys

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
    sys.exit(stcli.main())
