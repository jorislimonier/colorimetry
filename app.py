import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    name=__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.3, minimum-scale=0.5",
        }
    ],
)
server = app.server
