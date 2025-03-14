import sqlite3

def create_connection(db_path='data_warehouse.db'):
    """Create a database connection to SQLite3"""
    conn = sqlite3.connect(db_path)
    return conn

def aggregate_transactions(conn):
    """Aggregate transaction data for the gold layer (total, average, and count)"""
    cursor = conn.cursor()

    # Step 1: Aggregate transaction data from the bronze_transactions table
    cursor.execute('''
        SELECT customer_id,
               SUM(amount) AS total_amount,
               AVG(amount) AS avg_amount,
               COUNT(*) AS transaction_count
        FROM silver_transactions
        GROUP BY customer_id;
    ''')

    # Fetch all the aggregated data
    aggregated_data = cursor.fetchall()

    # Step 2: Insert the aggregated data into the gold_transactions table
    cursor.executemany('''
        INSERT INTO gold_transactions (customer_id, total_amount, avg_amount, transaction_count)
        VALUES (?, ?, ?, ?);
    ''', aggregated_data)

    conn.commit()
    print("Gold layer aggregation completed successfully!")

if __name__ == "__main__":
    conn = create_connection()
    aggregate_transactions(conn)
    conn.close()
