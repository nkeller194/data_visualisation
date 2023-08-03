import streamlit as st
import pandas as pd
import os
import numpy as np


file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)



st.write('Hello World')


el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])

from bokeh.plotting import figure

x = df['Mg']
y = df['Si']

p = figure(
    title='Element Scatter Plot',
    x_axis_label='Mg (wt%)',
    y_axis_label='Si (wt%)')

p.circle(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
