import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.sidebar.write("Interractive Widjets")

text = st.sidebar.text_input("あなたの好きな数字を教えてください")
condition = st.sidebar.slider("あなたの今の調子は", 0, 100, 50)
"あなたの趣味", text
"あなたの今の調子は？", condition
