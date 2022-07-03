import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("Interractive Widjets")

text = st.text_input("あなたの好きな数字を教えてください")
"あなたの趣味", text

condition = st.slider("あなたの今の調子は", 0, 100, 50)
"あなたの今の調子は？", condition
