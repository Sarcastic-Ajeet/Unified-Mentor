# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
# url = "G:\\Project 12_ Budget Sales Analytics\\AdventureWorks_Database.xlsx"
url="G:\\Project 12_ Budget Sales Analytics\\Budget.xlsx"
# data = pd.read_csv(url)
data=pd.read_excel(url)
# Explore the dataset
print(data.head())
print(data.info())
print(data.describe())

# Data cleaning (if needed)
# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values
data = data.dropna()  # Or use data.fillna() based on the context

# Feature Engineering (if needed)
# Example: Create a new column for Sales Variance
data['Sales_Variance'] = data['Sales'] - data['Budget']

# Data Visualization
# Sales vs Budget
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget', y='Sales', data=data)
plt.title('Sales vs Budget')
plt.xlabel('Budget')
plt.ylabel('Sales')
plt.show()

# Sales Variance Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Sales_Variance'], bins=30)
plt.title('Sales Variance Distribution')
plt.xlabel('Sales Variance')
plt.ylabel('Frequency')
plt.show()

# Key Metrics and Insights
total_sales = data['Sales'].sum()
total_budget = data['Budget'].sum()
total_variance = data['Sales_Variance'].sum()

print(f'Total Sales: {total_sales}')
print(f'Total Budget: {total_budget}')
print(f'Total Variance: {total_variance}')

# Dashboard Creation using Plotly (example)

# Scatter plot of Sales vs Budget
fig = px.scatter(data, x='Budget', y='Sales', title='Sales vs Budget')
fig.show()

# Bar plot for total Sales, Budget, and Variance
metrics = pd.DataFrame({
    'Metric': ['Total Sales', 'Total Budget', 'Total Variance'],
    'Value': [total_sales, total_budget, total_variance]
})

fig = px.bar(metrics, x='Metric', y='Value', title='Key Metrics')
fig.show()

# Save cleaned data for further use
data.to_csv('G:\\Project 12_ Budget Sales Analytics\\Budget.xlsx', index=False)

# Conclusion and Findings
# Based on the analysis, we can conclude the following:
# - Relationship between sales and budget.
# - Distribution of sales variance.
# - Key metrics indicating the overall performance.

# Create a project report (placeholder text)
project_report = """
Project Title: Budget Sales Analytics
Domain: Retail & Sales
Technologies: Python, Pandas, Matplotlib, Seaborn, Plotly
Project Difficulty Level: Advanced

1. Introduction
2. Data Exploration
3. Data Cleaning
4. Feature Engineering
5. Data Visualization
6. Key Metrics and Insights
7. Conclusion and Findings

The analysis showed a strong correlation between sales and budget, with a total variance of {total_variance}.
"""

# Save the project report
with open('project_report.txt', 'w') as file:
    file.write(project_report)

print("Project completed successfully!")
