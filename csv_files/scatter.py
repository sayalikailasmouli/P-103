import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv.csv")
fig = px.scatter(df, x='cases', y='date',
                 color='country', title='Corona Cases')
fig.show()
