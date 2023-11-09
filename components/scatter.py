from dash import dcc, html
import plotly.express as px

def render(app, data):
    fig = px.scatter(data, y='marketcap', x='country', size="marketcap")
    return html.Div(dcc.Graph(figure=fig),id="scatter-chart")