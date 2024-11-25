import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('iris.csv')
df.columns = ['sepal length', 'sepal width',
              'petal length', 'petal width', 'label']

df.dropna().reset_index(drop=True)

numeric_columns = df.iloc[:, :4]
z_scores = stats.zscore(numeric_columns)
z_scores_df = pd.DataFrame(z_scores, columns=numeric_columns.columns)
z_scores_df = z_scores_df.abs()


outliers = (z_scores > 3).any(axis=1)

print("Outliers in the DataFrame:")
print(df[outliers])
print("Corresponding z-scores:")
print(z_scores_df[outliers])

df_cleaned = df.copy()

mean_value = df.mode().iloc[0]
df[outliers] = mean_value


print("DataFrame after replacing outliers with mean value:")
print(df_cleaned[outliers])

df_cleaned.to_csv('cleanDup_iris.csv', index=False)
