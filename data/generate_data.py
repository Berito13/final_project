import os
import pandas as pd
import random
from faker import Faker
import pyarrow.parquet as pq
import pyarrow as pa

def generate_data(num_customers=10000, num_transactions=30000):
    """
    გენერირებს მომხმარებლებს, ტრანზაქციის ტიპებს და ტრანზაქციებს, შემდეგ კი ინახავს Parquet ფაილებში სწორ მონაცემთა ტიპებით.
    """

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # თუ __file__ მუშაობს
    except NameError:
        BASE_DIR = os.getcwd()  # როცა __file__ არ არის

    # აქ ვაყენებთ data საქაღალდის შიგნით sample საქაღალდეს
    output_dir = os.path.join(BASE_DIR, "data", "sample")

    # თუ sample საქაღალდე არ არსებობს, შევქმნათ
    os.makedirs(output_dir, exist_ok=True)

    fake = Faker()
    Faker.seed(42)

    # 1. Customers გენერაცია
    customers = [{"customer_id": i, "name": fake.name(), "email": fake.email(),
                  "location": fake.city(), "created_at": fake.date_time_this_decade()}
                 for i in range(1, num_customers + 1)]
    customers_df = pd.DataFrame(customers)

    # Datatypes-ის დასწორება
    customers_schema = pa.schema([
        ("customer_id", pa.int32()),
        ("name", pa.string()),
        ("email", pa.string()),
        ("location", pa.string()),
        ("created_at", pa.timestamp("ms"))  # datetime → timestamp
    ])

    # 2. Transaction Types გენერაცია
    transaction_types = ["purchase", "refund", "subscription", "chargeback", "transfer"]
    transaction_type_df = pd.DataFrame({
        "type_id": range(1, len(transaction_types) + 1),
        "type_name": transaction_types
    })

    transaction_types_schema = pa.schema([
        ("type_id", pa.int32()),
        ("type_name", pa.string())
    ])

    # 3. Transactions გენერაცია
    transactions = [{"transaction_id": i,
                     "customer_id": random.randint(1, num_customers),
                     "timestamp": fake.date_time_this_year(),
                     "amount": round(random.uniform(5.0, 500.0), 2),
                     "transaction_type": random.choice(transaction_types)}
                    for i in range(1, num_transactions + 1)]
    transactions_df = pd.DataFrame(transactions)

    transactions_schema = pa.schema([
        ("transaction_id", pa.int64()),
        ("customer_id", pa.int32()),
        ("timestamp", pa.timestamp("ms")),  # datetime → timestamp
        ("amount", pa.float32()),  # Ensure float type
        ("transaction_type", pa.string())
    ])

    # 4. მონაცემების ჩაწერა Parquet-ში სწორ მონაცემთა ტიპებით
    pq.write_table(pa.Table.from_pandas(customers_df, schema=customers_schema), os.path.join(output_dir, "customers.parquet"))
    pq.write_table(pa.Table.from_pandas(transaction_type_df, schema=transaction_types_schema), os.path.join(output_dir, "transaction_types.parquet"))
    pq.write_table(pa.Table.from_pandas(transactions_df, schema=transactions_schema), os.path.join(output_dir, "transactions.parquet"))

    print(f"✅ მონაცემები შეიქმნა {output_dir} ფოლდერში! (სწორი ტიპებით)")

if __name__ == "__main__":
    generate_data()
