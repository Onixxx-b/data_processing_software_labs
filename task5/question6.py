# Task 5. Graphics
import pyreadr as pr
import pandas as pd
from matplotlib import pyplot as plt

df1: pd.DataFrame = pr.read_r("../data/summarySCC_PM25.rds")[None]
df2: pd.DataFrame = pr.read_r("../data/Source_Classification_Code.rds")[None]

# Question 1
df1.groupby("year", as_index=False).sum("Emissions").plot(x="year", y="Emissions", kind="bar")

# Question 2
df1[df1["fips"] == "24510"].groupby("year", as_index=False).sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

# Question 3
fig, ax = plt.subplots(2, 2)
for i, t in enumerate(df1["type"].drop_duplicates().tolist()):
    df1[df1["type"] == t].groupby("year", as_index=False).sum("Emissions") \
        .plot(x="year", y="Emissions", kind="bar", ax=ax[int(i / 2), i % 2])
    ax[int(i / 2), i % 2].set_title(t)

sources = [i for i in df2[["SCC", "EI.Sector"]].to_dict().values()]
sources = {sources[0][i]: sources[1][i] for i in range(len(sources[0]))}
df1_2 = df1.apply(lambda x: x.apply(lambda y: sources[y]) if x.name == "SCC" else x)

# Question 4
df1_2[df1_2["SCC"].str.contains("Coal")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

# Question 5
df1_2[(df1_2["SCC"].str.startswith("Mobile")) & (df1_2["fips"] == "24510")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

# Question 6
df1_2[(df1_2["SCC"].str.startswith("Mobile")) & (df1_2["fips"] == "06037")] \
    .groupby("year", as_index=False) \
    .sum("Emissions") \
    .plot(x="year", y="Emissions", kind="bar")

plt.show()
