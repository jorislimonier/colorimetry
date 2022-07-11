from dash import dcc, html
import dash_bootstrap_components as dbc

dob_input = dbc.Select(
    id="dob_input",
    placeholder="Day of birth (DD)",
    options=[{"label": k, "value": k} for k in range(1, 32)],
    persistence=True,
    persistence_type="session",
)
mob_input = dbc.Select(
    id="mob_input",
    placeholder="Month of birth (MM)",
    options=[{"label": k, "value": k} for k in range(1, 13)],
    persistence=True,
    persistence_type="session",
)
yob_input = dbc.Select(
    id="yob_input",
    placeholder="Year of birth (YYYY)",
    options=[{"label": k, "value": k} for k in range(1925, 2026)],
    persistence=True,
    persistence_type="session",
)
firstname_input = dbc.Input(
    id="firstname_input",
    type="text",
    placeholder="First name",
    persistence=True,
    persistence_type="session",
)
lastname_input = dbc.Input(
    id="lastname_input",
    type="text",
    placeholder="Last name",
    persistence=True,
    persistence_type="session",
)

input_fields = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(dob_input, sm=4, md=3, lg=2),
                dbc.Col(mob_input, sm=4, md=3, lg=2),
                dbc.Col(yob_input, sm=4, md=3, lg=2),
            ],
            justify="center",
            style={"margin": "10px"},
        ),
        dbc.Row(
            children=[
                dbc.Col(firstname_input, sm=5, md=4, lg=3),
                dbc.Col(lastname_input, sm=5, md=4, lg=3),
            ],
            justify="center",
            style={"margin": "10px"},
        ),
    ],
)
