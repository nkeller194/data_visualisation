import streamlit as st
import pandas as pd
import os
import numpy as np


file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)



st.write('Hello World')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)


el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)



from bokeh.plotting import figure

x = st.selectbox('select element x_axis', el_list)
y = st.selectbox('select element y_axis', el_list)
st.multiselect('select location', file_name_list, file_name_list[0])
p = figure(
    title='Element Scatter Plot',
    x_axis_label = x + ' WT(%)',
    y_axis_label = y + ' WT(%)')

p.circle(df[x]/10000, df[y]/10000, legend_label='', line_width=2)
p.line([np.min(df[x]/10000), np.max(df[x]/10000)], [np.mean(df[y]/10000), np.mean(df[y]/10000)], legend_label = 'mean')
p.rect([np.min(df[x]/10000), np.max(df[x]/10000)], [np.std(df[y]/10000), np.std(df[y]/10000)], legend_label = 'Std', line_color = 'red')

st.bokeh_chart(p, use_container_width=True)
