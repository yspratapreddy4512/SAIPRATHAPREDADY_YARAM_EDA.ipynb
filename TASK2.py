# Merge customers with their transactions
customer_transactions = transactions.merge(customers, on='CustomerID')

# Merge the above result with products to get product details in each transaction
full_data = customer_transactions.merge(products, on='ProductID')

# Display the merged dataframe
print(full_data.head())
# Aggregate data to get customer profiles
customer_profile = full_data.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum',
    'ProductID': 'nunique',
    'Category': lambda x: x.mode()[0],  # Most frequently purchased category
    'Region': 'first'
}).reset_index()

# Display customer profile
print(customer_profile.head())
import csv

# Select the first 20 customers
customers_to_process = list(customer_ids)[:20]

# Prepare data for the Lookalike.csv file
lookalike_data = []
for customer_id in customers_to_process:
    lookalike_entry = [customer_id]
    for similar_customer, score in top_similar_customers[customer_id]:
        lookalike_entry.append((similar_customer, score))
    lookalike_data.append(lookalike_entry)

# Create the Lookalike.csv file
with open('FirstName_LastName_Lookalike.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CustomerID', 'Lookalike1', 'Score1', 'Lookalike2', 'Score2', 'Lookalike3', 'Score3'])
    for entry in lookalike_data:
        row = [entry[0]]
        for lookalike_tuple in entry[1:]:
            row.extend(lookalike_tuple)
        writer.writerow(row)

print("Lookalike.csv created successfully!")
import csv

# Select the first 20 customers
customers_to_process = list(customer_ids)[:20]

# Prepare data for the Lookalike.csv file
lookalike_data = []
for customer_id in customers_to_process:
    lookalike_entry = [customer_id]
    for similar_customer, score in top_similar_customers[customer_id]:
        lookalike_entry.append((similar_customer, score))
    lookalike_data.append(lookalike_entry)

# Create the Lookalike.csv file
with open('FirstName_LastName_Lookalike.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CustomerID', 'Lookalike1', 'Score1', 'Lookalike2', 'Score2', 'Lookalike3', 'Score3'])
    for entry in lookalike_data:
        row = [entry[0]]
        for lookalike_tuple in entry[1:]:
            row.extend(lookalike_tuple)
        writer.writerow(row)

print("Lookalike.csv created successfully!")
