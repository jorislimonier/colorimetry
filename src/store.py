from dash import Dash, dcc, html

store = html.Div( 
    children=[
        dcc.Store(id="birthdate_digit_store"),
        dcc.Store(id="fullname_digit_store"),
        dcc.Store(id="firstname_digits_store"),
        dcc.Store(id="lastname_digits_store"),
    ]
)
 