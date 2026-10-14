import streamlit as st

import requests

st.title(
    "AI Vehicle Damage Platform"
)

uploaded = st.file_uploader(
    "Upload Vehicle Image"
)

if uploaded:

    files = {

        "file": uploaded
    }

    result = requests.post(

        "http://localhost:8000/analyze",

        files=files

    ).json()

    st.write(result)