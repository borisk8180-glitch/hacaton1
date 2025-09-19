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