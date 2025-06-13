from prophet import Prophet
import pandas as pd

df = pd.read_csv('../data/train.csv')
df = df[df['Store'] == 1]  # Forecast for Store 1

# Prepare data for Prophet
df_prophet = df[['Date', 'Weekly_Sales']].rename(columns={'Date': 'ds', 'Weekly_Sales': 'y'})

# Model
model = Prophet()
model.fit(df_prophet)

# Future dates
future = model.make_future_dataframe(periods=12, freq='W')
forecast = model.predict(future)

# Save results
forecast[['ds', 'yhat']].to_csv('../data/store1_forecast.csv', index=False)
