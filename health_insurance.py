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

    # ===============================
# 3. Visualizations
# ===============================
# Histograms for numerical features
numeric_cols = ["age", "bmi", "charges"]
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    plt.hist(df[col], bins=30, edgecolor='k')
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

# Boxplot: Charges by smoker status
plt.figure(figsize=(6,4))
plt.boxplot([df[df["smoker"]=="yes"]["charges"], df[df["smoker"]=="no"]["charges"]],
            labels=["Smoker=Yes", "Smoker=No"])
plt.title("Charges by Smoker Status")
plt.ylabel("Charges")
plt.show()

# Scatter plot: BMI vs Charges, split by smoker
plt.figure(figsize=(8,6))
colors = df["smoker"].map({"yes": "red", "no": "blue"})
plt.scatter(df["bmi"], df["charges"], c=colors, alpha=0.6)
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.title("BMI vs Charges (red=smoker, blue=non-smoker)")
plt.show()

# ===============================
# 4. Correlation Matrix
# ===============================
# Convert categorical variables to numeric for correlation analysis
df_corr = df.copy()
df_corr["sex"] = df_corr["sex"].map({"male":1, "female":0})
df_corr["smoker"] = df_corr["smoker"].map({"yes":1, "no":0})
df_corr = pd.get_dummies(df_corr, columns=["region"], drop_first=False)

corr_matrix = df_corr.corr()
print("\n--- Correlation Matrix (selected columns) ---")
print(corr_matrix["charges"].sort_values(ascending=False))

# Heatmap (matplotlib imshow)
plt.figure(figsize=(8,6))
plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.title("Correlation Heatmap")
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.tight_layout()
plt.show()
