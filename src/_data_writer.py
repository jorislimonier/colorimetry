import pandas as pd

df = pd.read_excel("data/colors_meaning.xlsx", index_col=0)

with open("data/color_explanation.txt", "r") as f:
    txt = f.read()


clr_data = [[line for line in par.split("\n")] for par in txt.split("\n\n")]


arch1_titles = []
arch1_descriptions = []
arch2_titles = []
arch2_descriptions = []

for par in clr_data:
    color_title, arch1, arch2, kw = par
    arch1_title, arch1_description = arch1.split(" - ")
    arch2_title, arch2_description = arch2.split(" - ")

    arch1_titles.append(arch1_title)
    arch1_descriptions.append(arch1_description)
    arch2_titles.append(arch2_title)
    arch2_descriptions.append(arch2_description)

df["archetype1_title"] = arch1_titles
df["archetype1_description"] = arch1_descriptions
df["archetype2_title"] = arch2_titles
df["archetype2_description"] = arch2_descriptions

if False:
    df.to_excel("data/colors_meaning.xlsx")
