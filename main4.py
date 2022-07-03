import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit 超入門")

st.write("Interractive Widjets Image")

# True Falseを返す
# if st.checkbox("Show Image"):
#     img = Image.open("2007_000033.jpg")
#     st.image(img, caption="Kohei Imanishi", use_column_width=True)

option = st.selectbox(
    "あなたの好きな数字を教えてください",
    list(range(1,11))
)

"あなたの好きな数字は", option, "です"

