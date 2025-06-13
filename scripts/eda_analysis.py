import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/train.csv')

# Top 5 stores by average sales
top_stores = df.groupby('Store')['Weekly_Sales'].mean().sort_values(ascending=False).head()

# Plot
top_stores.plot(kind='bar', title='Top 5 Stores by Avg Sales')
plt.ylabel('Weekly Sales')
plt.tight_layout()
plt.show()
