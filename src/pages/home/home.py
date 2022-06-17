import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, html
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
        "border-radius": "10px",
    },
)
birthdate_title_display = html.H3(
    id="birthdate_title",
    style={
        "text-align": "center",
        "text-transform": "uppercase",
        "margin-top": "20px",
    },
)

birthdate_keywords_display = html.H4(
    children=[],
    id="birthdate_keywords",
    style={
        "text-align": "center",
        "margin-top": "20px",
    },
)

birthdate_results = dbc.Row(
    dbc.Col(
        children=[
            birthdate_color_display,
            birthdate_title_display,
            birthdate_keywords_display,
        ],
        width={"size": 10, "offset": 1},
    )
)

# Second row
color_glyph_container_firstname = dbc.Col(
    id="color_glyph_container_firstname",
    style={
        "display": "flex",
        "margin-bottom": "100px",
    },
)

color_glyph_container_lastname = dbc.Col(
    id="color_glyph_container_lastname",
    style={
        "display": "flex",
        "justify-content": "center",
    },
)

color_frequency_container = dbc.Col(
    id="color_frequency_container",
    style={},
)

second_row_container = html.Div(
    dbc.Row(
        children=[
            color_glyph_container_firstname,
            color_glyph_container_lastname,
            color_frequency_container,
        ],
        style={
            "justify-content": "center",
            "margin-top": "20px",
        },
    )
)

layout = [
    # title,
    input_fields,
    html.Br(),
    birthdate_results,
    html.Br(),
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
        title = f"{cd.color_digit} ─ {cd.title}"
        new_indicator_style["background-color"] = cd.color_code
        return title, new_indicator_style, cd.keywords
    else:
        new_indicator_style["background-color"] = BG_COLOR
        return "", new_indicator_style, ""


@callback(
    Output("color_glyph_container_firstname", "children"),
    Output("color_glyph_container_lastname", "children"),
    Output("color_glyph_container_firstname", "xl"),
    Output("color_glyph_container_lastname", "xl"),
    Output("color_frequency_container", "xl"),
    Output("color_glyph_container_firstname", "lg"),
    Output("color_glyph_container_lastname", "lg"),
    Output("color_frequency_container", "lg"),
    Output("color_glyph_container_firstname", "md"),
    Output("color_glyph_container_lastname", "md"),
    Output("color_frequency_container", "md"),
    Output("color_glyph_container_firstname", "sm"),
    Output("color_glyph_container_lastname", "sm"),
    Output("color_frequency_container", "sm"),
    Output("color_frequency_container", "children"),
    Input("firstname_input", "value"),
    Input("lastname_input", "value"),
)
def name_results(fn: str, ln: str) -> list:
    """Display the color glyph for firstname and lastname,
    as well as the color frequency:"""

    color_glyphs = color_glyph(fn), color_glyph(ln)
    color_freq = color_frequency(fn, ln)
    if fn is None or ln is None:
        fullname_length = 0
        firstname_span = 6
    else:
        print(fn, ln)
        fullname_length = len(f"{fn} {ln}")
        firstname_span = int(12 * len(fn) / fullname_length)
    lastname_span = 12 - firstname_span

    if fullname_length < 15:
        # firstname, lastname, frequency
        val = 1.4
        xl = firstname_span // 2, lastname_span // 2, 4
        lg = firstname_span // 2, lastname_span // 2, 4
        md = firstname_span // val, lastname_span // val, 10
        sm = 12, 12, 6
    elif fullname_length < 30:
        # firstname, lastname
        xl = firstname_span, lastname_span, 12
        lg = 10, 6, 6
        md = 12, 6, 6
        sm = 12, 12, 6
    else:
        # firstname, lastname
        xl = 10, 6, 12
        lg = 10, 6, 6
        md = 12, 6, 6
        sm = 12, 12, 6
    return *color_glyphs, *xl, *lg, *md, *sm, color_freq


def color_glyph(name: str):
    """Return the color glyph from a given name"""
    if name is None:
        return dash.no_update

    name_color_div = []

    for letter in name:
        style = {
            "width": "25px",
            "height": "180px",
            "justify": "center",
            "align-items": "center",
            "margin": "auto",
        }

        if letter == " ":  # add BG_COLOR div between names
            color = BG_COLOR

        else:  # get color for the given letter
            digit = utils.digit_from_str(letter)
            color = ColorData(digit).color_code
            style["box-shadow"] = ",".join(
                [
                    "0 1px 6px rgba(0, 0, 0, 0.1)",
                    "0 1px 4px rgba(0, 0, 0, 0.5)",
                ]
            )

        style["background-color"] = color

        # make div with appropriate color
        color_display = html.Div(style=style)

        # make div with uppercase letter
        letter_display = html.H3(
            children=letter.upper(),
            style={"text-align": "center"},
        )

        # concatenate color and letter divs
        div = dbc.Col(
            children=[color_display, letter_display],
            style={"margin-left": "1px"},
        )

        name_color_div.append(div)

    return name_color_div


def color_frequency(fn: str, ln: str) -> list:
    """Return the color glyph from first and last names"""
    if fn is None and ln is None:
        return dash.no_update
    if fn is None:
        fn = ""
    if ln is None:
        ln = ""

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
                "box-shadow": ",".join(
                    [
                        "0 1px 6px rgba(0, 0, 0, 0.1)",
                        "0 1px 4px rgba(0, 0, 0, 0.5)",
                    ]
                ),
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
            style={
                "display": "flex",
                "margin-left": "10%",
                # "justify-content": "center"
            },
        )

        color_frequency_div.append(div)

    return color_frequency_div
