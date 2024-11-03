import streamlit as st
from PIL import Image
import pandas as pd

st.title('管理ツール')
st.caption('これはテストアプリです。') 

image = Image.open('./data/スクリーンショット 2023-09-18 140023.png')
st.image(image, width=500)

df = pd.read_csv('./data/sample_utf8.csv', index_col='全国地方公共団体コード')

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df)
    
   
with col2:
    
    st.line_chart(df)

st.table(df)

dx = pd.read_excel('./data/【２０２３年】家計簿.xlsx')
st.dataframe(dx)