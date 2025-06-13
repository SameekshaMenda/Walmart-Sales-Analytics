# Walmart Sales Forecasting Project

## Overview
This project uses Walmart's store sales data to forecast weekly sales using Python and visualize insights using Power BI.

## Tech Stack
- Python (Pandas, Prophet, scikit-learn)
- MySQL
- Power BI

## Folder Structure
- `data/`: Raw datasets
- `scripts/`: Python code for loading, processing, modeling
- `mysql/`: SQL table setup
- `dashboard/`: Power BI .pbix files

## How to Run
1. Load CSVs into MySQL using `scripts/load_data_mysql.py`
2. Run `forecasting_model.py` to generate predictions
3. Export predictions and connect Power BI to MySQL
