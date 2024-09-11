#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:23:25 2024

@author: aidenguenther
"""
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import openpyxl


##Header
image = Image.open('Logo2.png')
max_size = (200, 200)
image.thumbnail(max_size)

col1, col2, col3 = st.columns(3)

with col1:
    st.title("Portfolio", anchor=False)

with col3:
    st.image(image)
    
##Excel Data
excel_file = 'CSProject_Data.xlsx'
sheet_name = 'Sheet2'

#Core Portfolio Table

start_row = 0
end_row = 14
df_corePortfolio = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:D',
                   header=0,
                   skiprows=range(0),
                   nrows=end_row - start_row)

#st.dataframe(df_corePortfolio)

#Active Portfolio Table

start_row2 = 18
end_row2 = 34
df_activePortfolio = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:D',
                   header=17,
                   skiprows=range(0),
                   nrows=end_row2 - start_row2)

#st.dataframe(df_activePortfolio)

#Core Portfolio Pie Chart

pie_chart = px.pie(df_corePortfolio,
                   title='Core Portfolio',
                   values=df_corePortfolio.columns[3],
                   names='Core Portfolio')
st.plotly_chart(pie_chart)


#Active Portfolio Pie Chart


pie_chart2 = px.pie(df_activePortfolio,
                   title='Active Portfolio',
                   values=df_activePortfolio.columns[3],
                   names='Active Portfolio')
st.plotly_chart(pie_chart2)

