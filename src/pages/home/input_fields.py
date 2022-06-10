from dash import dcc, html
import dash_bootstrap_components as dbc

dob_input = dbc.Select(
    id="dob_input",
    placeholder="Day of birth (DD)",
    options=[{"label": k, "value": k} for k in range(1, 32)],
    persistence=True,
    persistence_type="session",
    # value=12,
)
mob_input = dbc.Select(
    id="mob_input",
    placeholder="Month of birth (MM)",
    options=[{"label": k, "value": k} for k in range(1, 13)],
    persistence=True,
    persistence_type="session",
    # value=2,
)
yob_input = dbc.Select(
    id="yob_input",
    placeholder="Year of birth (YYYY)",
    options=[{"label": k, "value": k} for k in range(1925, 2026)],
    persistence=True,
    persistence_type="session",
    # value=1998,
)
firstname_input = dbc.Input(
    id="firstname_input",
    type="text",
    placeholder="First name",
    persistence=True,
    persistence_type="session",
    # value="Joris",
)
lastname_input = dbc.Input(
    id="lastname_input",
    type="text",
    placeholder="Last name",
    persistence=True,
    persistence_type="session",
    # value="LIMONIER",
)

input_fields = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(dob_input, width=2),
                dbc.Col(mob_input, width=2),
                dbc.Col(yob_input, width=2),
            ],
            justify="center",
            style={"margin": "10px"},
        ),
        dbc.Row(
            children=[
                dbc.Col(firstname_input, width=3),
                dbc.Col(lastname_input, width=3),
            ],
            justify="center",
            style={"margin": "10px"},
        ),
    ],
)
