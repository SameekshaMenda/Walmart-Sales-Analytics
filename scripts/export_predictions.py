import pandas as pd
import mysql.connector

df = pd.read_csv('../data/store1_forecast.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='walmart_sales'
)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS forecast_store1 (
        date DATE,
        predicted_sales FLOAT
    )
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO forecast_store1 (date, predicted_sales)
        VALUES (%s, %s)
    """, (
        row['ds'],
        row['yhat']
    ))

conn.commit()
cursor.close()
conn.close()
