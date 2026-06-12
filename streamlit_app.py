import streamlit as st
from streamlit.components.v1 import html
import pathlib

html_content = pathlib.Path("index.html").read_text(encoding="utf-8")

html(
    html_content,
    width=None,
    height=2000,
    scrolling=True
)
