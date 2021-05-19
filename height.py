import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv") 
fig = px.bar(x = df["Height(Inches)"].tolist(),y = df["Index"].tolist())
fig1 = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"]) 
fig.show()
fig1.show()