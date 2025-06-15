import pandas as pd
from forecasting_model import model  # Import your trained model
test_df = pd.read_csv("../data/test.csv")

# Feature Engineering
test_df['Date'] = pd.to_datetime(test_df['Date'])
test_df['Year'] = test_df['Date'].dt.year
test_df['Month'] = test_df['Date'].dt.month
test_df['Week'] = test_df['Date'].dt.isocalendar().week

features = ['Store', 'Dept', 'Year', 'Month', 'Week', 'IsHoliday']
X_test = test_df[features]

# Predict
test_df['Predicted_Sales'] = model.predict(X_test)
test_df.to_csv("../data/predictions.csv", index=False)

print("✅ Predictions exported to data/predictions.csv")
