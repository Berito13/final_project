import sqlite3

def create_connection(db_path=r'C:\Users\Administrator\PycharmProjects\final_project\data\data_warehouse.db'):
    """Create a database connection to SQLite3"""
    conn = sqlite3.connect(db_path)
    return conn

def create_tables(conn):
    """Create tables for bronze, silver, and gold layers"""
    cursor = conn.cursor()

    # Bronze Layer Table (raw data for transactions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bronze_transactions (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            timestamp TEXT,
            amount REAL,
            transaction_type TEXT
        );
    ''')

    # Bronze Layer Table (raw data for customers)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            location TEXT,
            created_at TEXT
        );
    ''')

    # Bronze Layer Table (raw data for transaction types)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transaction_types (
            type_id INTEGER PRIMARY KEY,
            type_name TEXT
        );
    ''')

    # Silver Layer Table (cleaned data for transactions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS silver_transactions (
            transaction_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            timestamp TEXT,
            amount REAL,
            transaction_type TEXT
        );
    ''')

    # Gold Layer Table (aggregated data for transactions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gold_transactions (
            customer_id INTEGER PRIMARY KEY,
            total_amount REAL,
            avg_amount REAL,
            transaction_count INTEGER
        );
    ''')

    conn.commit()
    print("Tables created successfully!")

if __name__ == "__main__":
    conn = create_connection()
    create_tables(conn)
    conn.close()
