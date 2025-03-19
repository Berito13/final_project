import sqlite3
import pandas as pd
import os


BASE_DIR = os.getcwd()

def load_bronze_data(conn, customers_parquet, transaction_types_parquet, transactions_parquet):
    """Ingest customer, transaction types, and transactions data into the bronze layer from Parquet files"""
    try:
        # Load customer data from Parquet
        customers_df = pd.read_parquet(customers_parquet)
        customers_df.to_sql('customers', conn, if_exists='replace', index=False)
        print(f"Successfully loaded customer data from {customers_parquet} into the bronze layer!")

        # Load transaction types data from Parquet
        transaction_types_df = pd.read_parquet(transaction_types_parquet)
        transaction_types_df.to_sql('transaction_types', conn, if_exists='replace', index=False)
        print(f"Successfully loaded transaction types data from {transaction_types_parquet} into the bronze layer!")

        # Load transaction data from Parquet
        transactions_df = pd.read_parquet(transactions_parquet)
        transactions_df.to_sql('bronze_transactions', conn, if_exists='replace', index=False)
        print(f"Successfully loaded transaction data from {transactions_parquet} into the bronze layer!")

    except Exception as e:
        print(f"Error loading data into bronze layer: {e}")

if __name__ == "__main__":
    # Adjust paths to your Parquet files
    customers_parquet = os.path.join(BASE_DIR, "data", "sample", "customers.parquet")
    transaction_types_parquet = os.path.join(BASE_DIR, "data", "sample", "transaction_types.parquet")
    transactions_parquet = os.path.join(BASE_DIR, "data", "sample", "transactions.parquet")

    conn = sqlite3.connect(os.path.join(BASE_DIR, "data", 'data_warehouse.db'))
    load_bronze_data(conn, customers_parquet, transaction_types_parquet, transactions_parquet)
    conn.close()
