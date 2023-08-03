import streamlit as st
import pandas as pd
import os
import matplotlib.pylpot as plt

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)



st.write('Hello World')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])


el_x = 'Mg'
el_y = 'Si'
plt.scatter(df[el_x], df[el_y])
plt.show()
