import pandas as pd
from scipy import stats as st

df = pd.read_csv("iris - dummy.csv")

df.columns = ["sepal length ", "sepal width", "petal length", "petal width", "lable"]
df = df.dropna().reset_index(drop=True)
data = df.iloc[:, :4]
labls = df["lable"]
zscors = st.zscore(data).abs()
threshhtold = 3
outliers = (zscors > threshhtold).any(axis=1)
modevalue = data["sepal width"].mode().iloc[0]
print(df.iloc[5:11])

df.to_csv("iris - cleaned.csv", index=False)
