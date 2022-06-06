import dash_bootstrap_components as dbc
from dash import html
from src.color_data import ColorData

COLOR_LIST = ColorData.data["color"].values
color_layout = {}

for color in COLOR_LIST:

    # get data for a given color
    color_data = ColorData.data[ColorData.data["color"] == color].iloc[0]

    title = html.H2(
        children=f"{color_data['color'].capitalize()} ─ Archétypes",
        style={"text-align": "center"},
    )

    archetype1_title = dbc.Col(
        html.H3(color_data["archetype1_title"].capitalize()), sm=5, md=5, lg=4
    )
    archetype2_title = dbc.Col(
        html.H3(color_data["archetype2_title"].capitalize()), sm=5, md=5, lg=4
    )
    archetype1_descr = dbc.Col(
        html.H6(color_data["archetype1_description"]), sm=9, md=11, lg=8
    )
    archetype2_descr = dbc.Col(
        html.H6(color_data["archetype2_description"]), sm=9, md=11, lg=8
    )

    color_layout[color] = html.Div(
        children=[
            title,
            dbc.Row(children=[archetype1_title, archetype1_descr]),
            dbc.Row(children=[archetype2_title, archetype2_descr]),
        ],
        style={"margin": " 20px"},
    )
