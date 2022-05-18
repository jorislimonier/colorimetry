import pandas as pd


class DataLoader:
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

    def __init__(self) -> None:
        self.data = pd.read_excel("data/colors_meaning.xlsx", index_col=0)
        self.data["color"] = self.data["color"].replace(self.COLORS_DICT)


if __name__ == "__main__":
    dl = DataLoader()
    # print(dl.data.loc[4])
