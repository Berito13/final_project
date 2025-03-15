import boto3
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from io import BytesIO

# AWS client initialization with the correct region (example: us-east-1)
s3 = boto3.client('s3', region_name='us-east-1')

def process_and_upload_gold(file_path, bucket_name):
    try:
        # Step 1: Download the processed Parquet file from the Silver bucket
        print(f"Downloading file from S3 bucket: {bucket_name}-silver-bucket/{file_path}")

        # Simulate downloading the file content from Silver bucket
        response = s3.get_object(Bucket=f"{bucket_name}-silver-bucket", Key=file_path)

        # Reading Parquet file directly from the S3 response
        file_content = response['Body'].read()

        # Create a BytesIO object to simulate a file object
        parquet_buffer = BytesIO(file_content)

        # Read the parquet file using pandas
        processed_data = pd.read_parquet(parquet_buffer)

        # Step 2: Aggregate or transform the data for Gold bucket (e.g., sum by category)
        # Example of a simple transformation (e.g., sum the data by a specific column)
        # For example, we could aggregate total sales per customer, product, etc.
        aggregated_data = processed_data.groupby('customer_id').agg({'amount': 'sum'}).reset_index()

        # Step 3: Create Gold bucket key (path) to upload the aggregated Parquet data
        gold_key = f"aggregated/business_ready/{file_path.split('/')[-1].replace('.parquet', '_aggregated.parquet')}"

        # Step 4: Convert the aggregated data to Parquet format and upload to Gold bucket
        table = pa.Table.from_pandas(aggregated_data)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)

        # Step 5: Upload aggregated Parquet data to Gold bucket
        s3.put_object(Bucket=f"{bucket_name}-gold-bucket", Key=gold_key, Body=parquet_buffer.getvalue())

        print(f"File successfully uploaded to Gold bucket: {bucket_name}-gold-bucket/{gold_key}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Simulate a file path and bucket name
    file_path = "processed/structured/transactions_processed.parquet"  # Example file path in Silver bucket
    bucket_name = "final-project"  # Your actual bucket name without "-silver"

    # Simulate processing and uploading to Gold
    process_and_upload_gold(file_path, bucket_name)
