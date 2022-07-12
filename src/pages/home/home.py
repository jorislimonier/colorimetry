import re

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, html
from dash.dependencies import Input, Output, State
from unidecode import unidecode
from src import utils
from src.color_data import ColorData
from src.components.input_fields import input_fields
from src.components.summary import summary_results
from src.constants import BG_COLOR, VOWELS


# Second row
color_glyph_container_firstname = dbc.Col(
    id="color_glyph_container_firstname",
    style={
        "display": "flex",
        "justifyContent": "center",
        "marginTop": "50px",
    },
)

color_frequency_container = dbc.Col(
    id="color_frequency_container",
    style={
        "justifyContent": "center",
        "display": "flex",
        "flex-direction": "column",
        "marginTop": "50px",
    },
)

second_row_container = html.Div(
    dbc.Row(
        children=[color_glyph_container_firstname, color_frequency_container],
        style={
            "justifyContent": "space-around",
            "marginTop": "20px",
        },
    )
)

layout = [
    input_fields,
    html.Br(),
    summary_results,
    html.Br(),
    second_row_container,
]

# ------ COLOR PATH ------
@callback(
    Output("color_path_section_title", "children"),
    Output("color_path_title", "children"),
    Output("color_path_section_color", "style"),
    Output("color_path_section_color_link", "href"),
    Output("color_path_section_keywords", "children"),
    Input("dob_input", "value"),
    Input("mob_input", "value"),
    Input("yob_input", "value"),
    State("color_path_section_color", "style"),
)
def color_path_section_color(dob, mob, yob, color_div_style):
    """Display birthdate color"""
    if dob is None or mob is None or yob is None:
        return dash.no_update

    digit = utils.digit_from_number(f"{dob}{mob}{yob}")
    new_color_div_style = color_div_style

    cd = ColorData(digit)

    if digit is not None:
        color_path_section_title = "Color path"
        title = f"{cd.color_digit} ─ {cd.title}"
        new_color_div_style["backgroundColor"] = cd.color_code
        color_href = f"/couleur/{unidecode(cd.color)}"

        return color_path_section_title, title, new_color_div_style, color_href, cd.keywords
    else:
        new_color_div_style["backgroundColor"] = BG_COLOR
        return "", "", new_color_div_style, "", ""


# ------ OUTER SELF ------
@callback(
    *[
        (
            Output(f"{prefix}_self_section_title", "children"),
            Output(f"{prefix}_self_title", "children"),
            Output(f"{prefix}_self_section_color", "style"),
            Output(f"{prefix}_self_section_color_link", "href"),
            Output(f"{prefix}_self_section_keywords", "children"),
        )
        for prefix in [
            "outer",
            "inner",
            "latent",
        ]
    ],
    Input("firstname_input", "value"),
    Input("lastname_input", "value"),
    State("outer_self_section_color", "style"),
    State("inner_self_section_color", "style"),
    State("latent_self_section_color", "style"),
)
def outer_self_section_color(
    fn: str,
    ln: str,
    outer_self_color_div_style: dict,
    inner_self_color_div_style: dict,
    latent_self_color_div_style: dict,
) -> tuple[str, str, dict, str]:
    """Display fullname color"""
    if fn is None or ln is None:
        return dash.no_update

    fn = unidecode(fn)
    ln = unidecode(ln)

    fn = re.sub(r"[^a-zA-Z]", "", fn)
    ln = re.sub(r"[^a-zA-Z]", "", ln)

    fullname = f"{fn}{ln}"

    outer_self_elements = section_elements(
        color_div_style=outer_self_color_div_style, start_string=fullname
    )

    start_string = "".join(c for c in fullname if c in VOWELS)
    inner_self_elements = section_elements(
        color_div_style=inner_self_color_div_style, start_string=start_string
    )

    start_string = "".join(c for c in fullname if c not in VOWELS)
    latent_self_elements = section_elements(
        color_div_style=latent_self_color_div_style, start_string=start_string
    )

    return (
        "Outer self",
        *outer_self_elements,
        "Inner self",
        *inner_self_elements,
        "Latent self",
        *latent_self_elements,
    )


def section_elements(color_div_style: dict, start_string: str) -> tuple[str, dict, str]:
    """Return elements for a section with color information"""
    digit = utils.digit_from_str(start_string)
    new_color_div_style = color_div_style

    cd = ColorData(digit)

    if 1 <= digit <= 9:
        title = f"{cd.color_digit} ─ {cd.title}"
        new_color_div_style["backgroundColor"] = cd.color_code
        color_href = f"/couleur/{unidecode(cd.color)}"
        return title, new_color_div_style, color_href, cd.keywords
        
    else:
        print("digit none")
        new_color_div_style["backgroundColor"] = BG_COLOR
        return "", new_color_div_style, "", ""


@callback(
    Output("color_glyph_container_firstname", "children"),
    Output("color_glyph_container_firstname", "xl"),
    Output("color_frequency_container", "xl"),
    Output("color_glyph_container_firstname", "lg"),
    Output("color_frequency_container", "lg"),
    Output("color_glyph_container_firstname", "md"),
    Output("color_frequency_container", "md"),
    Output("color_glyph_container_firstname", "sm"),
    Output("color_frequency_container", "sm"),
    Output("color_frequency_container", "children"),
    Input("firstname_input", "value"),
    Input("lastname_input", "value"),
)
def name_results(
    fn: str, ln: str
) -> tuple[list, int, int, int, int, int, int, int, int, int, int, int, int, list]:
    """Display the color glyph for firstname and lastname,
    as well as the color frequency:"""

    if fn is None or ln is None or fn == "" and ln == "":
        glyph = []
        color_freq = []
        fullname_length = 0
        dash.no_update

    else:
        fn = unidecode(fn)
        ln = unidecode(ln)

        fn = re.sub(r"[^a-zA-Z]", "", fn)
        ln = re.sub(r"[^a-zA-Z]", "", ln)

        glyph = color_glyph(f"{fn}{ln}")
        color_freq = color_frequency(fn, ln)

        fullname_length = len(f"{fn}{ln}")

    if fullname_length < 20:
        # name, frequency
        xl = 7, 5
        lg = 7, 5
        md = 10, 10
        sm = 12, 12
    else:
        # name, frequency
        xl = 12, 12
        lg = 12, 12
        md = 12, 12
        sm = 12, 12
    return glyph, *xl, *lg, *md, *sm, color_freq


def color_glyph(name: str) -> list:
    """Return the color glyph from a given name"""
    if name is None:
        return dash.no_update

    name_color_div = []

    for letter in name:
        style = {
            "width": "25px",
            "height": "180px",
            "justify": "center",
            "alignItems": "center",
            "margin": "auto",
        }

        if letter == " ":  # add BG_COLOR div between names
            color = BG_COLOR

        else:  # get color for the given letter
            digit = utils.digit_from_str(letter)
            color = ColorData(digit).color_code
            style["boxShadow"] = ",".join(
                [
                    "0 1px 6px rgba(0, 0, 0, 0.1)",
                    "0 1px 4px rgba(0, 0, 0, 0.5)",
                ]
            )

        style["backgroundColor"] = color

        # make div with appropriate color
        color_display = html.Div(style=style)

        # make div with uppercase letter
        letter_display = html.H3(
            children=letter.upper(),
            style={"textAlign": "center"},
        )

        # concatenate color and letter divs
        div = html.Div(
            children=[color_display, letter_display],
            style={
                "marginLeft": "0px",
                "display": "inline",
            },
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
                "backgroundColor": row["color_code"],
                "width": "30px",
                "height": "30px",
                "marginRight": "50px",
                "marginBottom": "15px",
                "boxShadow": ",".join(
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
                    "backgroundColor": row["color_code"],
                    "width": "30px",
                    "height": "30px",
                    "marginLeft": "10px",
                    "boxShadow": ",".join(
                        [
                            "0 1px 6px rgba(0, 0, 0, 0.1)",
                            "0 1px 4px rgba(0, 0, 0, 0.5)",
                        ]
                    ),
                }
            )
            for _ in range(row["count"])
        ]

        div = html.Div(
            children=[color_list, *color_frequency],
            style={"display": "flex", "marginLeft": "10%"},
        )

        color_frequency_div.append(div)

    return color_frequency_div
