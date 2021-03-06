import pandas as pd 

dataframe1 = pd.DataFrame(data=[("data1", "data2"), ("data3", "data4")], columns=["Column1", "Column2"])
print dataframe1

dataframe2 = pd.DataFrame(data=[("red", 2, "dog"), ("blue", 5, "cat"), ("red", 7, "fish")], columns=["Color", "Number", "Animal"])
print dataframe2

pivot_table = pd.pivot_table(dataframe2, values="Number", columns="Color", index="Animal")
print pivot_table

print dataframe2["Number"].sum()

print dataframe2.groupby("Color").groups

colors = dataframe2.groupby("Color").groups.keys()
print colors

for color in colors:
    print color


print dataframe2.groupby("Color").get_group("red")