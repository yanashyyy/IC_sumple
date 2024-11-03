import streamlit as st
from PIL import Image

st.title('管理ツール')
st.caption('これはテストアプリです。') 

image = Image.open('./data/スクリーンショット 2023-09-18 140023.png')
st.image(image, width=300)