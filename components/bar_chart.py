from dash import dcc, html
import plotly.express as px

def render(app, data):
    fig = px.bar(data, x='country', y='marketcap')
    return html.Div(dcc.Graph(figure=fig),id="bar-chart")