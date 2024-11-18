import pandas as pd

df = pd.read_csv('iris.csv')

df.columns = ['sepal length', 'sepal width',
              'petal length', 'petal width', 'label']

print("Shape of the DataFrame:", df.shape)
print("Count of each label:")
print(df['label'].value_counts())

duplicates = df[df.duplicated()]
print("Duplicate rows:\n", duplicates)

num_duplicates = df.duplicated().sum()
print("Number of duplicates:", num_duplicates)

df_cleaned = df.drop_duplicates(keep='last')

print("Shape of the cleaned DataFrame:", df_cleaned.shape)

df_cleaned.to_csv('cleanDup_iris.csv', index=False)
