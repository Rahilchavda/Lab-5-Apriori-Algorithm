# Import necessary libraries
from mlxtend.frequent_patterns import apriori
import pandas as pd
# Sample transactions (binary encoded)
transactions = [
['milk', 'bread', 'butter'],
['beer', 'bread'],
['milk', 'bread', 'beer'],
['milk', 'butter'],
['beer', 'butter']
]
# Convert transactions into a one-hot encoded DataFrame
all_items = sorted({item for transaction in transactions for
item in transaction})
# Create the one-hot encoded DataFrame
encoded_transactions = []
for transaction in transactions:
    encoded_transactions.append([1 if item in transaction else 0
for item in all_items])
df = pd.DataFrame(encoded_transactions, columns=all_items)
# Apply the Apriori algorithm to find frequent itemsets
min_support = 0.4 # Set minimum support
frequent_itemsets = apriori(df, min_support=min_support,
use_colnames=True)
# Display the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)