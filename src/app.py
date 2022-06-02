import dash_daq as daq
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from color_data import ColorData
import utils
import store
import input_fields
from callbacks import BG_COLOR

 
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

