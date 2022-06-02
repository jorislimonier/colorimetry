import dash_daq as daq
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import input_fields
import store
import utils
from callbacks import *
# from callbacks import BG_COLOR
from color_data import ColorData

# _______callbacks___________
import dash_daq as daq
import numpy as np
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State

from color_data import ColorData
import utils

BG_COLOR = "white"

 
# Store
## Birthdate digit
@callback(
    Output("birthdate_digit_store", "data"),
    Input("dob_input", "value"),
    Input("mob_input", "value"),
    Input("yob_input", "value"),
)
def store_birthdate_digit(dob, mob, yob):
    """Compute and store the color digit coming from birthdate"""
    is_valid = [isinstance(date, int) for date in [dob, mob, yob]]

    if np.all(is_valid):
        return utils.digit_from_number(f"{dob}{mob}{yob}")

    return None


## First name digits
@callback(
    Output("firstname_digits_store", "data"),
    Input("firstname_input", "value"),
)
def store_firstname_digits(fn):
    """Compute and store the color digit coming from fullname"""

    if isinstance(fn, str) and np.all([letter.isalpha() for letter in fn]):
        return [utils.digit_from_str(letter) for letter in fn]

    return None


## Last name digits
@callback(
    Output("lastname_digits_store", "data"),
    Input("lastname_input", "value"),
)
def store_lastname_digits(ln):
    """Compute and store the color digit coming from fullname"""

    if isinstance(ln, str) and np.all([letter.isalpha() for letter in ln]):
        return [utils.digit_from_str(letter) for letter in ln]

    return None


@callback(
    Output("birthdate_title", "children"),
    Output("birthdate_indicator", "style"),
    Output("birthdate_keywords", "children"),
    Input("birthdate_digit_store", "data"),
    State("birthdate_indicator", "style"),
)
def birthdate_color(digit, indicator_style):
    """Display birthdate color"""
    new_indicator_style = indicator_style
    cd = ColorData(digit)
    if digit is not None:
        new_indicator_style["background-color"] = cd.color_code
        return cd.title, new_indicator_style, cd.keywords
    else:
        new_indicator_style["background-color"] = BG_COLOR
        return "", new_indicator_style, ""

# ___________________________

# print(BG_COLOR)
title = html.H1("The Colour Path", style={"text-align": "center"})
birthdate_color_display = html.Div(
    id="birthdate_indicator",
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
    id="birthdate_keywords", style={"text-align": "center"}
)


app = Dash(__name__)
server = app.server
app.title = "The Colour Path"
app.layout = html.Div(
    children=(
        [title]
        + [input_fields.input_fields]
        + [birthdate_color_display]
        + [birthdate_title_display]
        + [birthdate_keywords_display]
        + [store.store]
    )
)


if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
    )
