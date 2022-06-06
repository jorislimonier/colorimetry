import dash_bootstrap_components as dbc
import unidecode
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app, server
from src.color_data import ColorData
from src.pages.colors import colors
from src.pages.home import home

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[dbc.DropdownMenuItem("Select a color", header=True)]
            + [
                dbc.DropdownMenuItem(
                    children=color.capitalize(),
                    href=f"/couleur/{unidecode.unidecode(color)}",
                )
                for color in ColorData.data["color"]
            ],
            nav=True,
            in_navbar=True,
            label="Couleurs",
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
def display_page(pathname: str):
    """Return the appropriate page layout, based on URL"""
    # return home page
    if pathname == "/":
        return home.layout

    # deal with colors that contain accents
    elif pathname == "/couleur/dore":
        return colors.color_layout["doré"]

    # return color page
    elif pathname.startswith("/couleur/"):
        color = pathname.removeprefix("/couleur/")
        return colors.color_layout[color]

    # page not found
    return "404 Page Error! Please enter a valid URL."


if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
    )
