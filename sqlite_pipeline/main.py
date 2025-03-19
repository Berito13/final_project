import sqlite3
import logging
from sqlite_pipeline.bronze_layer import load_bronze_data
from sqlite_pipeline.silver_layer import transform_silver_data
from sqlite_pipeline.gold_layer import aggregate_transactions
import os


BASE_DIR = os.getcwd()
database_path = os.path.join(BASE_DIR, "data", 'data_warehouse.db')
# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

def create_connection(db_path=database_path):
    """Create a database connection to SQLite3"""
    try:
        conn = sqlite3.connect(db_path)
        logging.info(f"Successfully connected to the database: {db_path}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        raise

def main():
    try:
        # Define file paths for Parquet files
        customers_parquet = os.path.join(BASE_DIR, "data", "sample", "customers.parquet")
        transaction_types_parquet = os.path.join(BASE_DIR, "data", "sample", "transaction_types.parquet")
        transactions_parquet = os.path.join(BASE_DIR, "data", "sample", "transactions.parquet")

        # Establish database connection
        conn = create_connection()

        # Step 1: Load data into the bronze layer (from Parquet files)
        logging.info("Loading data into the bronze layer...")
        load_bronze_data(conn, customers_parquet, transaction_types_parquet, transactions_parquet)

        # Step 2: Transform data into the silver layer (cleaned data)
        logging.info("Transforming data into the silver layer...")
        transform_silver_data(conn)

        # Step 3: Aggregate data into the gold layer (aggregated data)
        logging.info("Aggregating data into the gold layer...")
        aggregate_transactions(conn)

        # Close the database connection
        conn.close()
        logging.info("ETL pipeline completed successfully!")

    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")
        if conn:
            conn.close()
        logging.info("ETL pipeline aborted.")

if __name__ == "__main__":
    main()
