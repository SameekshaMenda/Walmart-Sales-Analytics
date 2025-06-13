import pandas as pd
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4SF22CD036",
    database="walmart_sales"
)
cursor = conn.cursor()
print("✅ Connected to MySQL!")


# Load CSVs
print("📂 Reading CSV files...")
stores_df = pd.read_csv("../data/stores.csv")
features_df = pd.read_csv("../data/features.csv").fillna(0)
train_df = pd.read_csv("../data/train.csv")
test_df = pd.read_csv("../data/test.csv")
print("✅ CSVs loaded successfully!")



# -----------------------------
# Insert into stores (batch)
print("📤 Inserting data into 'stores' table...")
stores_data = [
    (int(row['Store']), row['Type'], int(row['Size']))
    for _, row in stores_df.iterrows()
]
cursor.executemany(
    "INSERT INTO stores (Store, Type, Size) VALUES (%s, %s, %s)",
    stores_data
)

# -----------------------------
# Insert into features
print("📤 Inserting data into 'features' table...")
features_data = [
    (
        int(row['Store']), row['Date'], row['Temperature'], row['Fuel_Price'],
        row['MarkDown1'], row['MarkDown2'], row['MarkDown3'],
        row['MarkDown4'], row['MarkDown5'],
        row['CPI'], row['Unemployment'], bool(row['IsHoliday'])
    )
    for _, row in features_df.iterrows()
]
cursor.executemany("""
    INSERT INTO features (
        Store, Date, Temperature, Fuel_Price,
        MarkDown1, MarkDown2, MarkDown3, MarkDown4, MarkDown5,
        CPI, Unemployment, IsHoliday
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", features_data)
print(f"✅ Inserted {len(features_data)} rows into 'features'.")

# -----------------------------
# Insert into sales_train
print("📤 Inserting data into 'sales_train' table...")
sales_train_data = [
    (
        int(row['Store']), int(row['Dept']), row['Date'],
        row['Weekly_Sales'], bool(row['IsHoliday'])
    )
    for _, row in train_df.iterrows()
]
cursor.executemany("""
    INSERT INTO sales_train (Store, Dept, Date, Weekly_Sales, IsHoliday)
    VALUES (%s, %s, %s, %s, %s)
""", sales_train_data)
print(f"✅ Inserted {len(sales_train_data)} rows into 'sales_train'.")

# -----------------------------
# Insert into sales_test
print("📤 Inserting data into 'sales_test' table...")
sales_test_data = [
    (
        int(row['Store']), int(row['Dept']), row['Date'], bool(row['IsHoliday'])
    )
    for _, row in test_df.iterrows()
]
cursor.executemany("""
    INSERT INTO sales_test (Store, Dept, Date, IsHoliday)
    VALUES (%s, %s, %s, %s)
""", sales_test_data)
print(f"✅ Inserted {len(sales_test_data)} rows into 'sales_test'.")

# -----------------------------
# Final commit
print("💾 Committing changes to the database...")
conn.commit()
conn.close()
print("🎉 All data inserted successfully and connection closed.")
