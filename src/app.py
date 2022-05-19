import dash_daq as daq
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import data
import utils

BG_COLOR = "white"

app = Dash(__name__)
server = app.server
app.title = "Color for life"

app.layout = html.Div(
    children=[
        html.H1("Color for life", style={"text-align": "center"}),
        html.Div(
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
            style={"display": "flex", "wrap": "nowrap", "justify-content": "center"},
        ),
        html.H4(id="birthdate_digit"),
        html.H4(id="fullname_digit"),
        html.H4(id="firstname_digits"),
        html.H4(id="lastname_digits"),
        html.H4(id="letter_digits"),
        daq.Indicator(id="birthdate_indicator", color="red", label="", value=True),
        dcc.Store(id="birthdate_digit_store"),
        dcc.Store(id="fullname_digit_store"),
        dcc.Store(id="firstname_digits_store"),
        dcc.Store(id="lastname_digits_store"),
    ]
)


# Store
## Birthdate digit
@app.callback(
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


## First name digit
@app.callback(
    Output("firstname_digits_store", "data"),
    Input("firstname_input", "value"),
)
def store_firstname_digits(fn):
    """Compute and store the color digit coming from fullname"""

    if isinstance(fn, str) and np.all([letter.isalpha() for letter in fn]):
        return [utils.digit_from_str(letter) for letter in fn]

    return None


## Last name digit
## First name digit
@app.callback(
    Output("lastname_digits_store", "data"),
    Input("lastname_input", "value"),
)
def store_lastname_digits(ln):
    """Compute and store the color digit coming from fullname"""

    if isinstance(ln, str) and np.all([letter.isalpha() for letter in ln]):
        return [utils.digit_from_str(letter) for letter in ln]

    return None


# Display
## Birthdate digit
@app.callback(
    Output("birthdate_digit", "children"),
    Input("birthdate_digit_store", "data"),
)
def display_birthdate_digit(birthdate_digit):
    """Takes a birth date and returns its color digit"""
    if birthdate_digit is not None:
        return f"Your birthdate digit is: {birthdate_digit}"
    return None


## First name digit
@app.callback(
    Output("firstname_digits", "children"),
    Input("firstname_digits_store", "data"),
)
def display_firstname_digit(firstname_digit):
    """Takes a full name and returns its color digit"""
    if firstname_digit is not None:
        return f"Your first name digits are: {firstname_digit}"


## Last name digit
@app.callback(
    Output("lastname_digits", "children"),
    Input("lastname_digits_store", "data"),
)
def display_lastname_digits(lastname_digits):
    """Takes a full name and returns its color digit"""
    if lastname_digits is not None:
        return f"Your last name digits are: {lastname_digits}"


# @app.callback(
#     Output("letter_digits", "children"),
#     Input("firstname_input", "value"),
#     Input("lastname_input", "value"),
# )
# def digit_from_letters(fn, ln):
#     """Takes a full name and returns the color digit of each of its letters"""
#     if np.all([isinstance(letter, str) for letter in [fn, ln]]):
#         digits_fn = [utils.digit_from_str(letter) for letter in fn]
#         digits_ln = [utils.digit_from_str(letter) for letter in ln]
#         return f"Your letter digits are: {digits_fn} {digits_ln}"


@app.callback(
    Output("birthdate_indicator", "label"),
    Output("birthdate_indicator", "color"),
    Input("birthdate_digit", "children"),
)
def birthdate_color(digit):
    return "", BG_COLOR


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
