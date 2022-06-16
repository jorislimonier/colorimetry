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
            html.H4(color_data[f"archetype{row_idx}_title"].capitalize()),
            sm=5,
            md=5,
            lg={"size": 4, "offset": 1},
        )

        archetype_descr = dbc.Col(
            html.H6(color_data[f"archetype{row_idx}_description"]),
            sm=9,
            md=11,
            lg={"size": 6},
        )

        rows.append(
            dbc.Row(
                children=[archetype_title, archetype_descr],
                style={"margin-top": "30px"},
            )
        )

    rows.append(
        dbc.Row(
            dbc.Col(
                children=html.H3("Description du chemin de vie"),
                style={"text-align": "center", "margin-top": "30px"},
            ),
        )
    )
    rows.append(
        dbc.Row(
            dbc.Col(
                color_data["description"],
                width={"size": 10, "offset": 1},
            ),
            style={"margin-top": "20px"},
        ),
    )

    # rows.insert(3, html.Br())
    # rows.insert(2, html.Br())
    # rows.insert(1, html.Br())

    color_layout[color] = html.Div(
        children=[title, *rows],
        style={"margin": " 20px"},
    )
