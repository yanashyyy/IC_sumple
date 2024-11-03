import streamlit as st
from PIL import Image
import pandas as pd

st.title('管理ツール')
st.caption('これはテストアプリです。') 

image = Image.open('./data/スクリーンショット 2023-09-18 140023.png')
st.image(image, width=300)

df = pd.read_csv('./data/sample_utf8.csv', index_col='全国地方公共団体コード')

with st.dataframe(df):
    st.table(df)
    st.line_chart(df)

dx = pd.read_excel('./data/【２０２３年】家計簿.xlsx')
st.dataframe(dx)