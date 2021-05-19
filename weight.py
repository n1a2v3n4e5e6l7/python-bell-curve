import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv") 
fig = px.bar(x = df["Weight(Pounds)"].tolist(),y = df["Index"].tolist())
fig1 = ff.create_distplot([df["Weight(Pounds)"].tolist()],["WEIGHT"]) 
fig.show()
fig1.show()