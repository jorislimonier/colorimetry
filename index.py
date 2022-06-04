from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app, server
from src.pages import home

app.title = "The Colour Path"
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(
            children=[
                dcc.Link("Home", href="/"),
            ]
        ),
        html.Div(id="page-content", children=home.layout),
    ]
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/":
        return home.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == "__main__":
    app.run_server(
        debug=True,
        dev_tools_hot_reload=True,
    )
