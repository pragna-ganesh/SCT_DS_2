# README.md

# Titanic Dataset – Data Cleaning & Exploratory Data Analysis (EDA)

This project focuses on cleaning and analyzing the famous Titanic dataset.  
The script automatically extracts the dataset from a ZIP file, loads the CSV (train file), performs missing value handling, and visualizes multiple insights using Python.

---

## What this script does

• Unzips and loads the Titanic dataset  
• Cleans missing values (Age, Embarked, drops Cabin)  
• Prints basic dataset info and summary  
• Plots multiple visualizations including:

- Survival count  
- Survival by Gender  
- Age distribution  
- Class vs Survival  
- Age vs Fare relationship  
- Correlation heatmap  

---

## Requirements

Install dependencies:

bash
pip install pandas matplotlib seaborn

---

## Key Insights Observed

• Women had significantly higher survival rates
• 1st class passengers survived more than 3rd class
• Younger passengers had a slightly higher chance of survival
• Higher fares correlated with higher survival probability


---


## Purpose

This project was done to practice:

-Real-world dataset handling
-Cleaning and preprocessing
-Exploratory Data Analysis (EDA) techniques
-Data visualization with Python


---


## Output

Running this script will:

• Display dataset info & missing value summary in the terminal  
• Clean the dataset (Age, Embarked, remove Cabin)  
• Show multiple visual graphs such as:
  - Survival Count
  - Survival by Gender
  - Age Distribution
  - Survival by Passenger Class
  - Age vs Fare scatter plot
  - Correlation Heatmap

At the end, the terminal prints key insights extracted from the Titanic data.
