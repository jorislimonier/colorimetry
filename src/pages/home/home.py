import dash
from dash import callback, html
from dash.dependencies import Input, Output, State
import pandas as pd
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
    style={
        "width": "50%",
        "height": "100px",
        "display": "flex",
        "justify-content": "center",
    },
)

color_frequency_container = html.Div(
    id="color_frequency_container",
    style={
        "width": "50%",
        # "height": "100px",
        "margin": "auto",
        "justify-content": "center",
        # "background-color": "red",
    },
)

second_row_container = html.Div(
    children=[color_glyph_container, color_frequency_container],
    style={"height": "100px", "display": "flex"},
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
        style = {"width": "30px", "height": "30px"}
        
        if letter == " ": # add BG_COLOR div between names
            color = BG_COLOR

        else: # get color for the given letter
            digit = utils.digit_from_str(letter)
            color = ColorData(digit).color_code
            style[
                "box-shadow"
            ] = "0 1px 6px rgba(0, 0, 0, 0.1), 0 1px 4px rgba(0, 0, 0, 0.5)"

        style["background-color"] = color
        
        # make div with appropriate color
        color_display = html.Div(style=style)

        # make div with uppercase letter
        letter_display = html.H3(
            children=letter.upper(),
            style={"text-align": "center"},
        )

        # concatenate color and letter divs
        div = html.Div(
            children=[color_display, letter_display],
            style={"margin-left": "10px"},
        )

        fullname_color_div.append(div)

    return fullname_color_div


@callback(
    Output("color_frequency_container", "children"),
    Input("firstname_input", "value"),
    Input("lastname_input", "value"),
)
def color_frequency(fn, ln):
    """Return the color glyph from first and last names"""
    if (fn == "") or (ln == "") or (fn is None) or (ln is None):
        return dash.no_update

    color_frequency_div = []

    # initialize color count df
    color_count = ColorData.data[["color", "color_code"]].copy()
    color_count["count"] = 0
    for letter in f"{fn}{ln}":
        if letter == " ":
            # add BG_COLOR div between first and last names
            color = BG_COLOR
        else:
            # get color for the given letter
            digit = utils.digit_from_str(letter)
            color_count.loc[digit, "count"] += 1

    color_count = color_count.sort_values("count", ascending=False)

    for _, row in color_count.iterrows():
        # make div with appropriate color
        color_list = html.Div(
            style={
                "background-color": row["color_code"],
                "width": "30px",
                "height": "30px",
                "margin-right": "50px",
                "margin-bottom": "15px",
                "box-shadow": "0 1px 6px rgba(0, 0, 0, 0.1), 0 1px 4px rgba(0, 0, 0, 0.5)",
            }
        )

        color_frequency = [
            html.Div(
                style={
                    "background-color": row["color_code"],
                    "width": "30px",
                    "height": "30px",
                    "margin-left": "10px",
                    "box-shadow": "0 1px 6px rgba(0, 0, 0, 0.1), 0 1px 4px rgba(0, 0, 0, 0.5)",
                }
            )
            for _ in range(row["count"])
        ]

        div = html.Div(
            children=[color_list, *color_frequency],
            style={"display": "flex"},
        )

        color_frequency_div.append(div)

    return color_frequency_div
