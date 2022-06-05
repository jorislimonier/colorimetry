import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app, server
from src.color_data import ColorData
from src.pages.home import home

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[dbc.DropdownMenuItem("Select a color", header=True)]
            + [
                dbc.DropdownMenuItem(color.capitalize(), href=color)
                for color in ColorData.data["color_en"]
            ],
            nav=True,
            in_navbar=True,
            label="Colors",
        ),
    ],
    brand="The Colour Path",
    brand_href="/",
    color="primary",
    dark=True,
)
app.title = "The Colour Path"
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Div(id="page-content", children=home.layout),
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/":
        return home.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
    )
