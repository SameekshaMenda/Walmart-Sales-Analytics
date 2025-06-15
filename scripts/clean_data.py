import pandas as pd

# Load raw data
features_df = pd.read_csv("../data/features.csv")
train_df = pd.read_csv("../data/train.csv")

# Fill NA values with 0 or appropriate method
features_df.fillna(0, inplace=True)
train_df.dropna(inplace=True)

# Convert 'Date' to datetime
features_df['Date'] = pd.to_datetime(features_df['Date'])
train_df['Date'] = pd.to_datetime(train_df['Date'])

# Save cleaned versions
features_df.to_csv("../data/features.csv", index=False)
train_df.to_csv("../data/train.csv", index=False)

print("✅ Data cleaned and saved.")
