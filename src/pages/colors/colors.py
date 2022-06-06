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

    archetype1_title = html.H3(color_data["archetype1_title"].capitalize())
    archetype1_descr = html.H6(color_data["archetype1_description"])
    archetype2_title = html.H3(color_data["archetype2_title"].capitalize())
    archetype2_descr = html.H6(color_data["archetype2_description"])

    color_layout[color] = html.Div(
        children=[
            title,
            html.Div(children=[archetype1_title, archetype1_descr]),
            html.Div(children=[archetype2_title, archetype2_descr]),
        ],
    )
