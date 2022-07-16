import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, html, dcc
from src.constants import BG_COLOR

SECTION_TITLE_STYLE = {
    "textAlign": "center",
    # "textTransform": "uppercase",
    "marginTop": "20px",
}
COLOR_STYLE = {
    "backgroundColor": BG_COLOR,
    "width": "100px",
    "height": "100px",
    "margin": "20px auto 0",
    "borderRadius": "10px",
}
TITLE_STYLE = {
    "textAlign": "center",
    "textTransform": "uppercase",
    "marginTop": "20px",
}
KEYWORDS_STYLE = {
    "textAlign": "justify",
    "marginTop": "20px",
}


def color_section(section):
    section_title = html.H2(
        id=f"{section}_section_title",
        style=SECTION_TITLE_STYLE,
    )
    section_description = html.H4(
        id=f"{section}_section_description",
        style=SECTION_TITLE_STYLE,
    )
    section_color_display = dcc.Link(
        children=html.Div(
            id=f"{section}_section_color",
            style=COLOR_STYLE,
        ),
        id=f"{section}_section_color_link",
        href="",
    )
    section_title_display = html.H3(
        id=f"{section}_title",
        style=TITLE_STYLE,
    )

    section_keywords_display = html.H4(
        children=[],
        id=f"{section}_section_keywords",
        style=KEYWORDS_STYLE,
    )
    return dbc.Col(
        children=[
            section_title,
            section_description,
            section_color_display,
            section_title_display,
            section_keywords_display,
        ],
        md=5,
    )


summary_results = dbc.Row(
    children=[
        color_section("color_path"),
        color_section("outer_self"),
        color_section("inner_self"),
        color_section("latent_self"),
    ],
    style={"justifyContent": "space-around"},
)
