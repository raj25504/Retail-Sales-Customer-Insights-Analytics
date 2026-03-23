import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('retail_sales.csv')

# Data cleaning
df.drop_duplicates(inplace=True)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df.dropna(inplace=True)

# Calculate total sales for each row
df['TotalSales'] = df['Quantity'] * df['Price']

# Monthly sales trend
df['Month'] = df['OrderDate'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['TotalSales'].sum().reset_index()

plt.figure(figsize=(10,6))
plt.plot(monthly_sales['Month'], monthly_sales['TotalSales'], marker='o', color='cyan')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.title('Monthly Sales Trend', fontsize=16)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()

# Top performing products
product_sales = df.groupby('Product')['TotalSales'].sum().reset_index().sort_values(by='TotalSales', ascending=False)

plt.figure(figsize=(10,6))
plt.bar(product_sales['Product'], product_sales['TotalSales'], color=['blue', 'orange', 'green'])
plt.xlabel('Product', fontsize=14)
plt.ylabel('Total Sales', fontsize=14)
plt.title('Top Performing Products', fontsize=16)
plt.tight_layout()
plt.savefig('top_performing_products.png')
plt.show()
