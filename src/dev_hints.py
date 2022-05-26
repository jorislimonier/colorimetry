from dash.dependencies import Input, Output
from dash import callback

# Display
## Birthdate digit
@callback(
    Output("birthdate_digit", "children"),
    Input("birthdate_digit_store", "data"),
)
def display_birthdate_digit(birthdate_digit):
    """Takes a birth date and returns its color digit"""
    if birthdate_digit is not None:
        return f"Your birthdate digit is: {birthdate_digit}"
    return None


## First name digit
@callback(
    Output("firstname_digits", "children"),
    Input("firstname_digits_store", "data"),
)
def display_firstname_digit(firstname_digit):
    """Takes a full name and returns its color digit"""
    if firstname_digit is not None:
        return f"Your first name digits are: {firstname_digit}"


## Last name digit
@callback(
    Output("lastname_digits", "children"),
    Input("lastname_digits_store", "data"),
)
def display_lastname_digits(lastname_digits):
    """Takes a full name and returns its color digit"""
    if lastname_digits is not None:
        return f"Your last name digits are: {lastname_digits}"
