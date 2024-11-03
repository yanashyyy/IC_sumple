import streamlit as st
import pandas as pd


df = pd.read_csv('./data/sample_utf8.csv', index_col='全国地方公共団体コード')
st.dataframe(df)
st.table(df)
st.line_chart(df)

dx = pd.read_excel('./data/【２０２３年】家計簿.xlsx')
st.dataframe(dx)