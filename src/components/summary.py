import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, html
from src.constants import BG_COLOR

SECTION_TITLE_STYLE = {
    "textAlign": "center",
    "textTransform": "uppercase",
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
    "textAlign": "center",
    "marginTop": "20px",
}

# ------ COLOUR PATH ------
birthdate_section_title = html.H2(
    id="birthdate_section_title",
    style=SECTION_TITLE_STYLE,
)
birthdate_color_display = html.Div(
    id="birthdate_color",
    style=COLOR_STYLE,
)
birthdate_title_display = html.H3(
    id="birthdate_title",
    style=TITLE_STYLE,
)

birthdate_keywords_display = html.H4(
    children=[],
    id="birthdate_keywords",
    style=KEYWORDS_STYLE,
)

# ------ OUTER SELF ------
fullname_section_title = html.H2(
    id="fullname_section_title",
    style=SECTION_TITLE_STYLE,
)
fullname_color_display = html.Div(
    id="fullname_color",
    style=COLOR_STYLE,
)
fullname_title_display = html.H3(
    id="fullname_title",
    style=TITLE_STYLE,
)

fullname_keywords_display = html.H4(
    children=[],
    id="fullname_keywords",
    style=KEYWORDS_STYLE,
)

summary_results = dbc.Row(
    children=[
        dbc.Col(
            children=[
                birthdate_section_title,
                birthdate_color_display,
                birthdate_title_display,
                birthdate_keywords_display,
            ],
            width={"size": 5, "offset": 1},
        ),
        dbc.Col(
            children=[
                fullname_section_title,
                fullname_color_display,
                fullname_title_display,
                fullname_keywords_display,
            ],
            width={"size": 5},
        ),
    ]
)
