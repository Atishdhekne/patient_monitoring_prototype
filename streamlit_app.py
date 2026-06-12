import streamlit as st
from streamlit.components.v1 import html
import pathlib

st.set_page_config(
    page_title="Patient Monitoring Prototype",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_content = pathlib.Path("index.html").read_text(encoding="utf-8")

html(
    html_content,
    width=1920,
    height=4000,
    scrolling=True
)
