from dash import dcc, html

input_fields = html.Div(
    children=[
        dcc.Input(
            id="dob_input",
            type="number",
            placeholder="Day of birth (DD)",
            min=1,
            max=31,
            style={"margin": 15},
            # value=12,
        ),
        dcc.Input(
            id="mob_input",
            type="number",
            placeholder="Month of birth (MM)",
            min=1,
            max=12,
            style={"margin": 15},
            # value=2,
        ),
        dcc.Input(
            id="yob_input",
            type="number",
            placeholder="Year of birth (YYYY)",
            style={"margin": 15},
            # value=1998,
        ),
        dcc.Input(
            id="firstname_input",
            type="text",
            placeholder="First name",
            style={"margin": 15},
            # value="Joris",
        ),
        dcc.Input(
            id="lastname_input",
            type="text",
            placeholder="Last name",
            style={"margin": 15},
            # value="LIMONIER",
        ),
    ],
    style={
        "display": "flex",
        "wrap": "nowrap",
        "justify-content": "center",
    },
)
