from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server


app.layout = html.Div(
    children=[
        dcc.Input(
            id="input_text",
            type="text",
            placeholder="input type text",
        ),
        html.Div(
            id="out-all-types",
        ),
    ]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_text", "value")],
)
def cb_render(*vals):
    return vals


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True)
