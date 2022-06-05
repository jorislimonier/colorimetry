import pandas as pd


class ColorData:
    COLORS_DICT = {
        "rouge": "red",
        "orange": "orange",
        "jaune": "yellow",
        "vert": "green",
        "bleu": "blue",
        "indigo": "indigo",
        "violet": "purple",
        "rose": "#ff748c",
        "gold": "gold",
    }
    COLORS_FR_EN = {
        "rouge": "red",
        "orange": "orange",
        "jaune": "yellow",
        "vert": "green",
        "bleu": "blue",
        "indigo": "indigo",
        "violet": "purple",
        "rose": "pink",
        "gold": "gold",
    }

    data = pd.read_excel("data/colors_meaning.xlsx", index_col=0)
    data["color_en"] = data["color"].replace(COLORS_FR_EN)
    data["color_code"] = data["color"].replace(COLORS_DICT)

    def __init__(self, color_digit) -> None:
        self.color_digit = color_digit

    @property
    def title(self):
        return self.data.loc[self.color_digit, "title"]

    @property
    def color_code(self):
        return self.data.loc[self.color_digit, "color_code"]

    @property
    def color(self):
        return self.data.loc[self.color_digit, "color"]

    @property
    def keywords(self):
        return self.data.loc[self.color_digit, "keywords"]


if __name__ == "__main__":
    dl = ColorData(4)
    print(dl.keywords)
