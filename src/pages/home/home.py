from typing import Optional
import dash_daq as daq
import numpy as np
import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State

from src import utils
from src.color_data import ColorData
from src.pages.home.input_fields import input_fields

BG_COLOR = "white"


title = html.H1("The Colour Path", style={"text-align": "center"})


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

# Second row
color_glyph_container = html.Div(
    id="color_glyph_container",
    style={"width": "50%", "height": "100px", "display": "flex"},
)

second_row_container = html.Div(
    children=[color_glyph_container], style={"height": "100px"}
)

layout = [
    # title,
    input_fields,
    birthdate_color_display,
    birthdate_title_display,
    birthdate_keywords_display,
    second_row_container,
]


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


@callback(
    Output("color_glyph_container", "children"),
    Input("firstname_input", "value"),
    Input("lastname_input", "value"),
)
def color_glyph(fn, ln):
    """Return the color glyph from first and last names"""
    if (fn == "") or (ln == "") or (fn is None) or (ln is None):
        return dash.no_update

    fullname_color_div = []
    for letter in f"{fn} {ln}":
        if letter == " ":
            # add BG_COLOR div between first and last names
            color = BG_COLOR
        else:
            # get color for the given letter
            digit = utils.digit_from_str(letter)
            color = ColorData(digit).color_code

        # make div with appropriate color
        color_div = html.Div(
            style={
                "background-color": color,
                "width": "30px",
                "height": "30px",
            }
        )

        # make div with uppercase letter
        letter_div = html.H3(children=letter.upper(), style={"text-align": "center"})

        # concatenate color and letter divs
        div = html.Div(children=[color_div, letter_div])
        fullname_color_div.append(div)

    return fullname_color_div
