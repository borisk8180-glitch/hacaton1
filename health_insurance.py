import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Import dataset
# --------------------------
# (Assume file 'Medical Cost Personal Datasets.zip' is in the working directory)
# Now read csv-file
# Try reading with a different encoding if UTF-8 fails
try:
    # Assuming the csv file is extracted directly to the working directory
    df = pd.read_csv("insurance.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("insurance.csv", encoding='latin-1')


# Display first few rows to inspect
print(df.head())
print("\nDataset info:")
print(df.info())

# ===============================
# 2. Exploratory Data Analysis (EDA)
# ===============================
# Dataset info
print("\n--- Dataset Info ---")
print(df.info())

# Descriptive statistics for numerical columns
print("\n--- Descriptive Statistics ---")
print(df.describe().T)

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Value counts for categorical variables
for col in ["sex", "smoker", "region"]:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())