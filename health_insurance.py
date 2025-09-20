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