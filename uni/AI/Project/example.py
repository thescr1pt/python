import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1
df = pd.read_csv("heart_disease_uci.csv")

# Step 2
print("Checking for NaN values:\n", df.isna().any())
print("\nSummation of NaN values in each column:\n", df.isnull().sum() * 100 / len(df))
print("\nChecking for duplicated records:\n", df.duplicated().sum())

# Type of each column
print(df.info())

# Imputing numerical_columns with (mean)
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
numerical_columns_with_nan = [col for col in numerical_columns if df[col].isna().any()]
imputer = SimpleImputer(strategy="mean")
df[numerical_columns_with_nan] = imputer.fit_transform(df[numerical_columns_with_nan])

# Imputing categorical_columns with most frequent category
categorical_columns = df.select_dtypes(include=["object", "category"]).columns
imp = SimpleImputer(strategy="most_frequent")
df[categorical_columns] = imp.fit_transform(df[categorical_columns])

print("\nSummation of NaN values in each column:\n", df.isnull().sum() * 100 / len(df))

# Dropping ID because its not useful for ML
df = df.drop("id", axis=1)

# Step 3
# Label Encoding
pd.set_option("future.no_silent_downcasting", True)
df["gender"] = df["gender"].replace({"Male": 1, "Female": 0}).astype(int)

df["cp"] = (
    df["cp"]
    .replace(
        {"typical angina": 0, "atypical angina": 1, "non-anginal": 2, "asymptomatic": 3}
    )
    .astype(int)
)

df["restecg"] = (
    df["restecg"]
    .replace({"normal": 0, "st-t abnormality": 1, "lv hypertrophy": 2})
    .astype(int)
)

df["slope"] = (
    df["slope"].replace({"upsloping": 0, "flat": 1, "downsloping": 2}).astype(int)
)

df["thal"] = (
    df["thal"]
    .replace({"fixed defect": 0, "normal": 1, "reversable defect": 2})
    .astype(int)
)

label_encoder = LabelEncoder()
df["dataset"] = label_encoder.fit_transform(df["dataset"])
df["fbs"] = label_encoder.fit_transform(df["fbs"])
df["exang"] = label_encoder.fit_transform(df["exang"])

print(df)

# Data scaling
min_max_scaler = MinMaxScaler()
original_numerical_columns = ["age", "trestbps", "chol", "thalch", "oldpeak", "ca"]
df[original_numerical_columns] = min_max_scaler.fit_transform(
    df[original_numerical_columns]
)

target_counts = df["num"].value_counts()
print("\nClass distribution in target variable:")
print(target_counts)

sns.countplot(x="num", data=df)
plt.title("Class Distribution of Target Variable")
plt.show()

target_percentage = target_counts / len(df) * 100
print("\nPercentage distribution of target variable classes:")
print(target_percentage)

X = df.drop("num", axis=1)
y = df["num"]

smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

print("\nClass distribution after applying SMOTE:")
print(pd.Series(y_res).value_counts())

under_sampler = RandomUnderSampler(random_state=42)
X_res_under, y_res_under = under_sampler.fit_resample(X, y)

# Check the class distribution after undersampling
print("\nClass distribution after applying Under-sampling:")
print(pd.Series(y_res_under).value_counts())

pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_res)

# Check the shape of the new data after PCA
print("\nShape of data after PCA transformation:")
print(X_pca.shape)

# Step 4
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", cbar=True, square=True)
plt.title("Heart Disease")
plt.show()
print(df)

correlation_matrix = correlation_matrix.abs()
uppertriangle = np.triu(np.ones(correlation_matrix.shape), k=1)
correlation_matrix = correlation_matrix.where(uppertriangle == 1)

redundant = []

for column in correlation_matrix.columns:
    if any(correlation_matrix[column] > 0.8):
        redundant.append(column)

df.drop(columns=redundant, inplace=True)
