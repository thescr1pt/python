import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("heart_disease_uci.csv")
# df = df.dropna().reset_index(drop=True)


new = df.iloc[:, 0]
columnnames = df.columns.tolist()
for i in range(1, 16):
    target = df.iloc[:, i]
    if type(df.iloc[1, i]) == str:
        target = LabelEncoder().fit_transform(target)
        target = pd.DataFrame(target, columns=[columnnames[i]])

    new = pd.concat([new, target], axis=1)

print(new)

# correlation_matrix = df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", cbar=True, square=True)
# plt.title("Correlation Heatmap of Iris Dataset Features")
# plt.show()
