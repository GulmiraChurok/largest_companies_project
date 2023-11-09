from dash import dcc, html
import plotly.express as px

def render(app, data):
    fig = px.bar(data, x='marketcap', y='country', orientation='h')
    return html.Div(dcc.Graph(figure=fig),id="hor_bar-chart")