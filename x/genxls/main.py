import pandas as pd

data = [
    ["0-6", 34],
    ["6-12", 54],
    ["13-16", 34],
    ["17-18", 134],
    ["18-80", 34],
]

df = pd.DataFrame(data)
df.to_excel("output.xlsx")
