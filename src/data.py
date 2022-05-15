import pandas as pd


class DataLoader:
    def __init__(self) -> None:
        self.data = pd.read_excel("data/colors_meaning.xlsx", index_col=0)


if __name__ == "__main__":
    dl = DataLoader()
    print(dl.data)
