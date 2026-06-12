import streamlit as st
from streamlit.components.v1 import html
import pathlib

st.set_page_config(
    page_title="Patient Monitoring Prototype",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu, header, footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    padding: 0rem !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)

html_content = pathlib.Path("index.html").read_text(encoding="utf-8")

html(
    html_content,
    height=900,
    scrolling=True
)
