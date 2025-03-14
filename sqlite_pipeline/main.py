import sqlite3
from sqlite_pipeline.bronze_layer import load_bronze_data
from sqlite_pipeline.silver_layer import transform_silver_data
from sqlite_pipeline.gold_layer import aggregate_transactions

def create_connection(db_path=r'C:\Users\Administrator\PycharmProjects\final_project\data\data_warehouse.db'):
    """Create a database connection to SQLite3"""
    conn = sqlite3.connect(db_path)
    return conn

def main():
    # Define file paths for Parquet files
    customers_parquet = r'C:\Users\Administrator\PycharmProjects\final_project\data\sample\customers.parquet'
    transaction_types_parquet = r'C:\Users\Administrator\PycharmProjects\final_project\data\sample\transaction_types.parquet'
    transactions_parquet = r'C:\Users\Administrator\PycharmProjects\final_project\data\sample\transactions.parquet'

    # Establish database connection
    conn = create_connection()

    # Step 1: Load data into the bronze layer (from Parquet files)
    print("Loading data into the bronze layer...")
    load_bronze_data(conn, customers_parquet, transaction_types_parquet, transactions_parquet)

    # Step 2: Transform data into the silver layer (cleaned data)
    print("Transforming data into the silver layer...")
    transform_silver_data(conn)

    # Step 3: Aggregate data into the gold layer (aggregated data)
    print("Aggregating data into the gold layer...")
    aggregate_transactions(conn)

    # Close the database connection
    conn.close()

    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    main()
