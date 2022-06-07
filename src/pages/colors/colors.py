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

    title_width = {"sm": 5, "md": 5, "lg": 4}
    descr_width = {"sm": 9, "md": 11, "lg": 8}

    rows = []
    for row_idx in range(1, 3):
        archetype_title = dbc.Col(
            html.H3(color_data[f"archetype{row_idx}_title"].capitalize()),
            sm=title_width["sm"],
            md=title_width["md"],
            lg=title_width["lg"],
        )

        archetype_descr = dbc.Col(
            html.H6(color_data[f"archetype{row_idx}_description"]),
            sm=descr_width["sm"],
            md=descr_width["md"],
            lg=descr_width["lg"],
        )

        rows.append(dbc.Row(children=[archetype_title, archetype_descr]))
    
    rows.insert(1, html.Br())
    
    color_layout[color] = html.Div(
        children=[title, *rows],
        style={"margin": " 20px"},
    )
