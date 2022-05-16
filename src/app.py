from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_daq as daq
import numpy as np
import utils


BG_COLOR = "white"

app = Dash(__name__)
server = app.server


app.layout = html.Div(
    children=[
        dcc.Input(id="dob", type="number", placeholder="Day of birth", min=1, max=31),
        dcc.Input(id="mob", type="number", placeholder="Month of birth", min=1, max=12),
        dcc.Input(id="yob", type="number", placeholder="Year of birth"),
        dcc.Input(id="firstname", type="text", placeholder="First name"),
        dcc.Input(id="lastname", type="text", placeholder="Last name"),
        html.H4(id="birthdate_digit"),
        html.H4(id="fullname_digit"),
        html.H4(id="letter_digits"),
        daq.Indicator(id="birthdate_indicator", color=BG_COLOR, label="", value=False),
    ]
)


@app.callback(
    Output("birthdate_digit", "children"),
    Input("dob", "value"),
    Input("mob", "value"),
    Input("yob", "value"),
)
def digit_from_birthdate(*vals):
    """Takes a birth date and returns its color digit"""
    dob, mob, yob = vals
    if np.all([isinstance(date, int) for date in vals]):
        digit = utils.digit_from_number(f"{dob}{mob}{yob}")
        return f"Your birthdate digit is: {digit}"


@app.callback(
    Output("fullname_digit", "children"),
    Input("firstname", "value"),
    Input("lastname", "value"),
)
def digit_from_fullname(*vals):
    """Takes a full name and returns its color digit"""
    fn, ln = vals
    if np.all([isinstance(name, str) for name in vals]):
        digit = utils.digit_from_str(f"{fn}{ln}")
        return f"Your full name digit is: {digit}"


@app.callback(
    Output("letter_digits", "children"),
    Input("firstname", "value"),
    Input("lastname", "value"),
)
def digit_from_letters(*vals):
    """Takes a full name and returns the color digit of each of its letters"""
    fn, ln = vals
    if np.all([isinstance(letter, str) for letter in vals]):
        digits_fn = " ".join([str(utils.digit_from_str(letter)) for letter in fn])
        digits_ln = " ".join([str(utils.digit_from_str(letter)) for letter in ln])
        return f"Your letter digits are: {digits_fn} {digits_ln}"


@app.callback(
    Output("birthdate_indicator", "label"),
    Output("birthdate_indicator", "color"),
    Input("birthdate_digit", "children"),
)
def birthdate_color(digit):
    print(digit)
    return "", BG_COLOR


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
