import plotly.graph_objects as go  # or plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv("di.csv")
token = open(".mapbox_token").read()
colors = ["#306998", "#FFD43B"] * 10
tf = dict(family="sans serif", size=14, color=colors[0])

fig = go.Figure(
    go.Scattermapbox(
        mode="markers+text",
        lon=data.lon,
        lat=data.lat,
        marker={"size": 20, "color": colors},
        text="🐍 " + data.name,
        textfont=tf,
        textposition="bottom right",
    )
)

fig.update_layout(
    mapbox={"accesstoken": token, "style": "streets", "zoom": 0.5}, showlegend=False
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

app = dash.Dash()
app.layout = html.Div([dcc.Graph(figure=fig)])

# app.run_server(debug=True, use_reloader=False)
app.run_server()
