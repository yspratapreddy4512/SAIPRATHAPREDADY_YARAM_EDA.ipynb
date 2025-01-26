# Merge customers and transactions datasets
customer_transactions = transactions.merge(customers, on='CustomerID')

# Aggregate data to get customer profiles with transaction info
customer_profile = customer_transactions.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum',
    'ProductID': 'nunique',
    'SignupDate': 'first',
    'Region': 'first'
}).reset_index()

# Convert SignupDate to numerical format
customer_profile['SignupDate'] = pd.to_datetime(customer_profile['SignupDate'])
customer_profile['SignupYear'] = customer_profile['SignupDate'].dt.year
customer_profile = customer_profile.drop(columns=['SignupDate'])

# Encode categorical variables: Region
customer_profile = pd.get_dummies(customer_profile, columns=['Region'], drop_first=True)

# Display the prepared customer profile data
print(customer_profile.head())
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Normalize the feature data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_profile.drop(columns=['CustomerID']))

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
customer_profile['Cluster'] = kmeans.fit_predict(scaled_features)

# Display the clusters assigned
print(customer_profile.head())
from sklearn.metrics import davies_bouldin_score

# Calculate Davies-Bouldin Index
db_index = davies_bouldin_score(scaled_features, customer_profile['Cluster'])
print(f"Davies-Bouldin Index: {db_index}")
import matplotlib.pyplot as plt
import seaborn as sns
import umap

# Use UMAP for dimensionality reduction to 2D
reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(scaled_features)

# Create a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], hue=customer_profile['Cluster'], palette='viridis')
plt.title('Customer Segmentation using UMAP')
plt.xlabel('UMAP Dimension 1')
plt.ylabel('UMAP Dimension 2')
plt.show()
