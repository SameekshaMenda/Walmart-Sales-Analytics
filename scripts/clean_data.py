import pandas as pd

df = pd.read_csv('../data/train.csv')
print(df.isnull().sum())

# Fill missing values if needed
df.fillna(0, inplace=True)

df.to_csv('../data/train_cleaned.csv', index=False)
print("✅ Cleaned data saved.")
