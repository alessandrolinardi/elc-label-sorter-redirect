import streamlit as st

new_url = "https://elc-frontend.onrender.com/pickup"

st.warning("⚠️ This tool has moved!")
st.markdown(f"### [Click here to go to the new tool]({new_url})")

st.components.v1.html(
    f'<script>window.top.location.href = "{new_url}";</script>',
    height=0,
)
