import sqlite3
import pandas as pd

import os


BASE_DIR = os.getcwd()
database_path = os.path.join(BASE_DIR, "data", 'data_warehouse.db')
def transform_silver_data(conn):
    """Transform and clean the data for the silver layer"""
    try:
        # Query the raw data from bronze layer
        query = 'SELECT * FROM bronze_transactions'
        raw_data = pd.read_sql(query, conn)

        # Example transformation: Ensure no missing amounts and clean the transaction_type column
        cleaned_data = raw_data.dropna(subset=['amount'])
        cleaned_data['transaction_type'] = cleaned_data['transaction_type'].str.strip().str.lower()

        # Insert cleaned data into silver table
        cleaned_data.to_sql('silver_transactions', conn, if_exists='replace', index=False)
        print("Successfully transformed and loaded data into the silver layer!")
    except Exception as e:
        print(f"Error transforming data for silver layer: {e}")

if __name__ == "__main__":
    conn = sqlite3.connect(database_path)
    transform_silver_data(conn)
    conn.close()
