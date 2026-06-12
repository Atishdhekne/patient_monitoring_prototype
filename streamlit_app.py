import streamlit as st
import pathlib

st.set_page_config(
    page_title="Patient Monitoring Prototype",
    page_icon="🏥",
    layout="wide"
)

html_content = pathlib.Path("index.html").read_text(encoding="utf-8")

st.components.v1.html(
    html_content,
    height=900,
    scrolling=True
)
