import plotly.graph_objects as go  # or plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import parsenvy
import base64

data = pd.read_csv("di.csv")
# token = open(".mapbox_token").read()
token = parsenvy.str("mapbox_token")
colors = ["#306998", "#FFD43B"] * 10
tf = dict(family="sans serif", size=14, color=colors[0])

fig_map = go.Figure(
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

fig_map.update_layout(
    mapbox={"accesstoken": token, "style": "streets", "zoom": 0.5}, showlegend=False
)
fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

image_filename = "psf-logo-wiki.png"
encoded_image = base64.b64encode(open(image_filename, "rb").read())
# Launch the application:
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            className="header-title",
            children=[
                html.Div(
                    html.Img(
                        src="data:image/png;base64,{}".format(encoded_image.decode())
                    ),
                    style={"width": "20%", "display": "inline-block"},
                ),
                html.Div(
                    html.H2(
                        id="title",
                        children="Diversity and Inclusion Working Group",
                    ),
                    style={"width": "80%", "display": "inline-block"},
                ),
            ],
            style={
                "box-shadow": "rgb(240, 240, 240) 5px 5px 5px 0px",
            },
        ),
        html.Div(
            children="The Diversity and Inclusion Working Group is a volunteer workgroup of the Python Software Foundation."
        ),
        html.A(
            "Official announcement",
            href="https://wiki.python.org/psf/DiversityandInclusionWG",
        ),
        html.Div(children="This dashboard was done with the occasion of the IWD 2021"),
        html.Div(children="#ChooseToChallenge"),
        html.Br(),
        html.Div(
            children="On this map you can see all the members of the group as of March 2021"
        ),
        dcc.Graph(id="id_map", figure=fig_map),
    ],
    style={
        "font-family": "Courier New, monospace",
        "width": 1200,
        "height": 800,
        "max-width": "100%",
    },
)

# app.run_server(debug=True, use_reloader=False)

# Add the server clause:
if __name__ == "__main__":
    app.run_server()
