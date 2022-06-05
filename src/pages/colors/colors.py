from dash import dcc, html
from src.color_data import ColorData


COLOR_LIST = ColorData.data["color_en"].values
color_layout = {}

for color in COLOR_LIST:
    color_data = ColorData.data[ColorData.data["color_en"] == color]
    print(color_data.iloc[0].values)
    color_layout[color] = html.Div([val for val in color_data.iloc[0]])