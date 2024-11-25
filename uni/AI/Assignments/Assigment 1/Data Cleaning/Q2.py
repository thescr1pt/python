import pandas as pd

df = pd.read_csv('iris.csv')
df.columns = ['sepal length', 'sepal width',
              'petal length', 'petal width', 'label']

print("Shape of the dataset:", df.shape)

null_columns = df.columns[df.isnull().any()]
null_counts = df[null_columns].isnull().sum()
print("Null values in each column:")
print(null_counts)

print("Columns with null values:")
print(df[null_columns])

df = df.fillna(df.mode().iloc[0])

print("Selected columns after imputation:")
print(df[null_columns])

print("DataFrame after imputation:")
print(df)

df.to_csv('cleanDup_iris.csv', index=False)
