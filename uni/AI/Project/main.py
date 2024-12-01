import pandas as pd
import numpy as np
from scipy import stats as st
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.decomposition import PCA


# 1: Import Dataset
df = pd.read_csv("heart_disease_uci.csv")

# 2: Data Cleaning
# Missing values
print("Missing values:\n", df.isna().any())
# Duplicates
print("\nDuplicates:\n", df.duplicated().sum())
