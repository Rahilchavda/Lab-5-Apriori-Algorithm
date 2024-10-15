import numpy as np
import pandas as pd

# Define the items in the store
items = ['milk', 'bread', 'eggs', 'cookies', 'soda', 'beer', 'diapers', 'juice', 'fruit', 
         'cheese', 'yogurt', 'cereal', 'chips', 'ice cream', 'pizza', 'pasta', 'rice', 
         'beans', 'chocolate', 'candy']

# Set the number of transactions and number of items per transaction
num_transactions = 20
max_items_per_transaction = 2

# Generate random transactions
transactions = []
for _ in range(num_transactions):
    num_items = np.random.randint(1, max_items_per_transaction + 1)  # Random number of items in each transaction
    transaction = np.random.choice(items, num_items, replace=False).tolist()  # Randomly select items for the transaction
    transaction += [''] * (max_items_per_transaction - len(transaction))  # Fill with empty strings if fewer than 20 items
    transactions.append(transaction)

# Convert to DataFrame
df = pd.DataFrame(transactions)

# Save the DataFrame to a CSV file
df.to_csv('apriori_store_data.csv', index=False, header=False)

print("CSV file 'apriori_store_data.csv' created successfully.")
