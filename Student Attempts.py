import pandas as hi
import csv
import plotly.graph_objects as pgo

dataframe = hi.read_csv('data.csv')

student_df = dataframe.loc[dataframe['student_id']== 'TRL_987']

print(student_df.groupby('level')['attempt'].mean())

fig = pgo.Figure(pgo.Scatter(
    x = student_df.groupby('level')['attempt'].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],
    orientation = 'h'
))

fig.show()