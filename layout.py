from dash import html
import dash_bootstrap_components as dbc
from components import pie_chart, bar_chart, hor_bar_chart, scatter

def create_layout(app,data):
    return dbc.Container(
        [
            pie_chart.render(app,data),
            bar_chart.render(app,data),
            hor_bar_chart.render(app,data),
            scatter.render(app,data)
        ]
    )
