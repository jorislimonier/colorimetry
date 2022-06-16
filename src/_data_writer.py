import pandas as pd
import yaml

df = pd.read_excel("data/colors_meaning.xlsx", index_col=0)

with open("data/color_explanation.txt", "r") as f:
    txt = f.read()

with open("data/color_description.yaml", "r") as stream:
    color_descr: dict = yaml.safe_load(stream=stream)


arch1_titles = []
arch1_descriptions = []
arch2_titles = []
arch2_descriptions = []
keywords_list = []
description_list = []

colors = [*color_descr]

for color in colors:
    archetype1_title, archetype1_description = color_descr[color]["archetype1"].values()
    archetype2_title, archetype2_description = color_descr[color]["archetype2"].values()

    keywords = color_descr[color]["keywords"]
    description = color_descr[color]["description"]

    arch1_titles.append(archetype1_title)
    arch1_descriptions.append(archetype1_description)
    arch2_titles.append(archetype2_title)
    arch2_descriptions.append(archetype2_description)
    keywords_list.append(keywords)
    description_list.append(description)
    # df[df["color"] == color][color_attributes]
print(df)

df["archetype1_title"] = arch1_titles
df["archetype1_description"] = arch1_descriptions
df["archetype2_title"] = arch2_titles
df["archetype2_description"] = arch2_descriptions
df["keywords"] = keywords_list
df["description"] = description_list

print(df)

# clr_data = [[line for line in par.split("\n")] for par in txt.split("\n\n")]




# for par in clr_data:
#     color_title, arch1, arch2, kw = par
#     arch1_title, arch1_description = arch1.split(" - ")
#     arch2_title, arch2_description = arch2.split(" - ")

#     arch1_titles.append(arch1_title)
#     arch1_descriptions.append(arch1_description)
#     arch2_titles.append(arch2_title)
#     arch2_descriptions.append(arch2_description)


if True:
    df.to_excel("data/colors_meaning.xlsx")
