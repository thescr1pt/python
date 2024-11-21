import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt


# Q1 READ DATA SET
df = pd.read_csv("iris - dummy.csv")

# Insert names for columns because they have no names
df.columns = ["sepal width", "sepal length", "petal width", "petal length", "label"]

# Q2 Drop all null values and reset all the spaces in the dataset
df = df.dropna().reset_index(drop=True)

# Cut out the data into a numerical part and a string part
numerical = df.iloc[:, :4]
labels = df["label"]

# Q3 Apply MinMax to numerical values
scaled = MinMaxScaler().fit_transform(numerical)

# Turn the MinMax values back into a data fram because they got converted to a 2d array in the last step
numerical = pd.DataFrame(
    scaled, columns=numerical.columns
)  # Don't forget to give it the column names

# Put the new scaled numerical values next to the old string values to complete the dataset
new_df = pd.concat([numerical, labels], axis=1)

# Create correlation matrix
correlation_matrix = numerical.corr()

# Q4 Display Correlation matrix in a heat map
plt.figure(figsize=(12, 8))
sns.heatmap(data=correlation_matrix, cmap="Greens", cbar=True, annot=True)
plt.show()

# Q5 write the new data fram with the scaled values into a new file
new_df.to_csv("iris - fixed")
