import pandas as pd
from scipy import stats as st

df = pd.read_csv("iris - dummy.csv")
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "label"]

df = df.dropna().reset_index(drop=True)

data = df.iloc[:, :4]
labels = df["label"]

zscores = st.zscore(data).abs()

threshold = 3

outliers = (zscores > threshold).any(axis=1)

modeValue = data["sepal width"].mode().iloc[0]

df.loc[zscores["sepal width"] > threshold, "sepal width"] = modeValue

print(df.iloc[5:11])

df.to_csv("iris - cleaned.csv", index=False)
