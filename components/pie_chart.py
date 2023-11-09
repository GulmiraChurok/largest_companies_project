from dash import dcc, html
import plotly.express as px

def render(app, data):
    fig = px.pie(data, values='marketcap', names='country', title='Countries by marketcap')
    return html.Div(dcc.Graph(figure=fig),id="pie-chart")