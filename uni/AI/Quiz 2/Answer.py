import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

Heart_df = pd.read_csv("heart_disease_uci.csv")

numerical = Heart_df.select_dtypes(include=["int64", "float64"]).columns
categorical = Heart_df.select_dtypes(include=["object"]).columns

for col in categorical:
    le = LabelEncoder()
    Heart_df[col] = Heart_df[col].astype(str)
    Heart_df[col] = le.fit_transform(Heart_df[col])

scaler = MinMaxScaler()
Heart_df[numerical] = scaler.fit_transform(Heart_df[numerical])

correlation_matrix = Heart_df.corr()
plt.figure(figsize=(12, 8))

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", cbar=True, square=True)
plt.title("Heart Disease")
plt.show()

correlation_matrix = correlation_matrix.abs()

upperTri = np.triu(np.ones(correlation_matrix.shape), k=1).astype(np.bool)

correlation_matrix = correlation_matrix.where(upperTri)

redundant = list()
for column in correlation_matrix.columns:
    if any(correlation_matrix[column] > 0.95):
        redundant.append(column)


Heart_df.drop(redundant, axis=1, inplace=True)

print(Heart_df)
