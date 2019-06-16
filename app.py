import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import plotly
import plotly.graph_objs as go

dash_app = dash.Dash()
app = dash_app.server

df = pd.read_csv('data.csv',header=None,sep= " ")

layout = plotly.graph_objs.Layout(
    title="Temperature and Humidity",
    xaxis={"title":"Time"},
    yaxis={"title":"Degree"},
)

temperature = go.Scatter(
                x=df[0].index,
                y=df[0],
                name = "Temperature",
                line = dict(color="yellow"),
                opacity = 0.8)

humidity = go.Scatter(
                x=df[1].index,
                y=df[1],
                name = "Humidity",
                line = dict(color="black"),
                opacity = 0.8)

data = [temperature, humidity]

dash_app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        This is made by Dash!
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    dash_app.run_server(debug=True)
