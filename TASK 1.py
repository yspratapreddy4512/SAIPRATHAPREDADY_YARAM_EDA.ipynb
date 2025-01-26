import pandas as pd

# Load datasets
customers = pd.read_csv('path_to_customers.csv')
products = pd.read_csv('path_to_products.csv')
transactions = pd.read_csv('path_to_transactions.csv')

# Display first few rows of each dataframe
print(customers.head())
print(products.head())
print(transactions.head())
# Check for missing values
print(customers.isnull().sum())
print(products.isnull().sum())
print(transactions.isnull().sum())

# Check data types
print(customers.dtypes)
print(products.dtypes)
print(transactions.dtypes)

# Remove duplicates if any
customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
transactions.drop_duplicates(inplace=True)
print(transactions.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# Customer Signups over Time
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
sns.lineplot(x=customers['SignupDate'].dt.year, y=customers['CustomerID'].groupby(customers['SignupDate'].dt.year).count())
plt.title('Customer Signups Over Time')
plt.ylabel('Number of Signups')
plt.show()

# Product Category Distribution
sns.countplot(y=products['Category'])
plt.title('Product Category Distribution')
plt.show()

# TotalValue Distribution
sns.histplot(transactions['TotalValue'], bins=30)
plt.title('Distribution of Transaction Total Value')
plt.show()
