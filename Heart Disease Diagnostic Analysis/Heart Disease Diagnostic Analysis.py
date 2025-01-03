import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

# Load dataset (replace 'heart_disease_data.csv' with your actual file path)
data = pd.read_csv('F:\Project 10_ Heart Disease Diagnostic Analysis project\Heart Disease data.csv')

# Display first few rows of the dataset
data.head()
# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values if necessary
data = data.dropna()

# Display dataset information
data.info()

# Count plot of heart disease
plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=data)
plt.title('Distribution of Heart Disease')
plt.xlabel('Heart Disease (1 = Yes, 0 = No)')
plt.ylabel('Count')
plt.show()

# Count plot of heart disease by gender
plt.figure(figsize=(10, 6))
sns.countplot(x='sex', hue='target', data=data)
plt.title('Heart Disease by Gender')
plt.xlabel('Gender (1 = Male, 0 = Female)')
plt.ylabel('Count')
plt.legend(title='Heart Disease', loc='upper right')
plt.show()

# Age distribution with heart disease
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='age', hue='target', multiple='stack', bins=30)
plt.title('Heart Disease by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Correlation matrix
corr_matrix = data.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Scatter plot for cholesterol and heart disease
plt.figure(figsize=(10, 6))
sns.scatterplot(x='chol', y='age', hue='target', data=data, palette='viridis')
plt.title('Cholesterol vs Age by Heart Disease')
plt.xlabel('Cholesterol')
plt.ylabel('Age')
plt.show()

def load_data(filepath):
    """Load the dataset from the given file path."""
    return pd.read_csv(filepath)

data = load_data('F:\Project 10_ Heart Disease Diagnostic Analysis project\Heart Disease data.csv')
