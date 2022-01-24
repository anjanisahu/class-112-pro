import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
prapti=pd.read_csv("data_story.csv")
fig=px.scatter(prapti, y="quant_saved",color="rem_any")
fig.show()

