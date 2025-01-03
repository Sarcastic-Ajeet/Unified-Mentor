import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'Amazon Sales data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Drop or fill missing values
df.dropna(inplace=True)  # Or df.fillna(method='ffill', inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year
df['Order Year-Month'] = df['Order Date'].dt.to_period('M')



# Month-wise Sales Trend
month_sales = df.groupby('Order Month')['Sales Channel'].sum().reset_index()
sns.lineplot(data=month_sales, x='Order Month', y='Sales Channel')
plt.title('Month-wise Sales Trend')
plt.show()

# Year-wise Sales Trend
year_sales = df.groupby('Order Year')['Sales Channel'].sum().reset_index()
sns.lineplot(data=year_sales, x='Order Year', y='Sales Channel')
plt.title('Year-wise Sales Trend')
plt.show()

# Year-Month-wise Sales Trend
year_month_sales = df.groupby('Order Year-Month')['Sales Channel'].sum().reset_index()
year_month_sales['Order Year-Month'] = year_month_sales['Order Year-Month'].astype(str)
sns.lineplot(data=year_month_sales, x='Order Year-Month', y='Sales Channel')
plt.xticks(rotation=90)
plt.title('Year-Month-wise Sales Trend')
plt.show()

# Top Products by Sales
top_products = df.groupby('Item Type')['Sales Channel'].sum().sort_values(ascending=False).head(10)
print(top_products)

# Sales by Category
category_sales = df.groupby('Item Type')['Sales Channel'].sum().sort_values(ascending=False)
print(category_sales)

# Sales by Region
region_sales = df.groupby('Region')['Sales Channel'].sum().sort_values(ascending=False)
print(region_sales)
