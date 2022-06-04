from typing import Optional
import dash_daq as daq
import numpy as np
import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State

from src import utils
from src.color_data import ColorData

BG_COLOR = "white"

# store = html.Div(
#     children=[
#         dcc.Store(id="birthdate_digit_store"),
#         dcc.Store(id="fullname_digit_store"),
#         dcc.Store(id="firstname_digits_store"),
#         dcc.Store(id="lastname_digits_store"),
#     ]
# )


title = html.H1("The Colour Path", style={"text-align": "center"})

input_fields = html.Div(
    children=[
        dcc.Input(
            id="dob_input",
            type="number",
            placeholder="Day of birth (DD)",
            min=1,
            max=31,
            style={"margin": 15},
        ),
        dcc.Input(
            id="mob_input",
            type="number",
            placeholder="Month of birth (MM)",
            min=1,
            max=12,
            style={"margin": 15},
        ),
        dcc.Input(
            id="yob_input",
            type="number",
            placeholder="Year of birth (YYYY)",
            style={"margin": 15},
        ),
        dcc.Input(
            id="firstname_input",
            type="text",
            placeholder="First name",
            style={"margin": 15},
        ),
        dcc.Input(
            id="lastname_input",
            type="text",
            placeholder="Last name",
            style={"margin": 15},
        ),
    ],
    style={
        "display": "flex",
        "wrap": "nowrap",
        "justify-content": "center",
    },
)

birthdate_color_display = html.Div(
    id="birthdate_color",
    style={
        "background-color": BG_COLOR,
        "width": "100px",
        "height": "100px",
        "margin": "auto",
    },
)
birthdate_title_display = html.H3(
    id="birthdate_title",
    style={"text-align": "center", "text-transform": "uppercase"},
)

birthdate_keywords_display = html.H4(
    children=[], id="birthdate_keywords", style={"text-align": "center"}
)

layout = (
    # [store]
    [title]
    + [input_fields]
    + [birthdate_color_display]
    + [birthdate_title_display]
    + [birthdate_keywords_display]
)

# Store
## First name digits
# @callback(
#     Output("firstname_digits_store", "data"),
#     Input("firstname_input", "value"),
# )
# def store_firstname_digits(fn):
#     """Compute and store the color digit coming from fullname"""

#     if isinstance(fn, str) and np.all([letter.isalpha() for letter in fn]):
#         return [utils.digit_from_str(letter) for letter in fn]

#     return None


## Last name digits
# @callback(
#     Output("lastname_digits_store", "data"),
#     Input("lastname_input", "value"),
#     # prevent_initial_call=True,
# )
# def store_lastname_digits(ln):
#     """Compute and store the color digit coming from fullname"""

#     if isinstance(ln, str) and np.all([letter.isalpha() for letter in ln]):
#         return [utils.digit_from_str(letter) for letter in ln]

#     return None


@callback(
    Output("birthdate_title", "children"),
    Output("birthdate_color", "style"),
    Output("birthdate_keywords", "children"),
    Input("dob_input", "value"),
    Input("mob_input", "value"),
    Input("yob_input", "value"),
    State("birthdate_color", "style"),
)
def birthdate_color(dob, mob, yob, indicator_style):
    """Display birthdate color"""
    if dob is None or mob is None or yob is None:
        return dash.no_update

    digit = utils.digit_from_number(f"{dob}{mob}{yob}")
    new_indicator_style = indicator_style

    cd = ColorData(digit)
    if digit is not None:
        new_indicator_style["background-color"] = cd.color_code
        return cd.title, new_indicator_style, cd.keywords
    else:
        new_indicator_style["background-color"] = BG_COLOR
        return "", new_indicator_style, ""
