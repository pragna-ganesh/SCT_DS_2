# ---------------------------------------------
# Titanic Dataset - Data Cleaning and EDA
# ---------------------------------------------

import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Unzip the dataset
zip_path = "titanic.zip"
extract_path = "titanic_data"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

# Load CSV file (automatically detect which one to use)
# Prefer loading 'train.csv' if available
for file in os.listdir(extract_path):
    if "train" in file.lower() and file.endswith(".csv"):
        csv_path = os.path.join(extract_path, file)
        break


# Load dataset
df = pd.read_csv(csv_path)

print("✅ Dataset Loaded Successfully!")
print(f"Shape: {df.shape}")
print("\nPreview:")
print(df.head())

# ---------------------------------------------
# 1️⃣ Basic Information and Missing Values
# ---------------------------------------------
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# ---------------------------------------------
# 2️⃣ Data Cleaning
# ---------------------------------------------
# Fill missing 'Age' with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing 'Embarked' with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' due to excessive missing data
if 'Cabin' in df.columns:
    df.drop('Cabin', axis=1, inplace=True)

print("\nAfter Cleaning Missing Values:")
print(df.isnull().sum())

# ---------------------------------------------
# 3️⃣ Exploratory Data Analysis (EDA)
# ---------------------------------------------
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Survival count
sns.countplot(x='Survived', data=df, palette='viridis')
plt.title("Survival Count", fontsize=14)
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()

# Survival by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='Sex', hue='Survived', data=df, palette='coolwarm')
plt.title("Survival by Gender", fontsize=14)
plt.show()

# Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True, color='skyblue')
plt.title("Age Distribution", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Class vs Survival
plt.figure(figsize=(10, 6))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='mako')
plt.title("Survival by Passenger Class", fontsize=14)
plt.show()

# Age vs Fare (Relationship)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, palette='Set1', alpha=0.7)
plt.title("Age vs Fare (Colored by Survival)", fontsize=14)
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap", fontsize=14)
plt.show()

# ---------------------------------------------
# 4️⃣ Insights Summary
# ---------------------------------------------
print("\n🔍 Key Insights:")
print("""
1. Survival Rate: More passengers did not survive (around 62% non-survivors).
2. Gender: Females had a much higher survival rate than males.
3. Class: Passengers in 1st class survived more than those in 3rd class.
4. Age: Younger passengers had a slightly higher chance of survival.
5. Fare: Higher fare values correlated positively with survival (wealthier passengers had better outcomes).
""")
