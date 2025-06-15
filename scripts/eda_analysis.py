import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv("../data/train.csv")

# Sales distribution
sns.histplot(train_df['Weekly_Sales'], bins=50, kde=True)
plt.title("Distribution of Weekly Sales")
plt.show()

# Sales over time
train_df['Date'] = pd.to_datetime(train_df['Date'])
sales_by_date = train_df.groupby("Date")['Weekly_Sales'].sum()
sales_by_date.plot(figsize=(12,5), title="Total Weekly Sales Over Time")
plt.ylabel("Weekly Sales")
plt.show()
