import boto3
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from io import BytesIO

# AWS client initialization with the correct region (example: us-east-1)
s3 = boto3.client('s3', region_name='us-east-1')

def process_and_upload_parquet(file_path, bucket_name):
    try:
        # Step 1: Download the raw Parquet file from the Bronze bucket
        print(f"Downloading file from S3 bucket: {bucket_name}/{file_path}")

        # Simulate downloading the file content
        response = s3.get_object(Bucket=f"{bucket_name}-bronze-bucket", Key=file_path)

        # Reading Parquet file directly from the S3 response
        file_content = response['Body'].read()

        # Create a BytesIO object to simulate a file object
        parquet_buffer = BytesIO(file_content)

        # Read the parquet file using pandas
        raw_data = pd.read_parquet(parquet_buffer)

        # Step 2: Process data (e.g., drop missing values, duplicates, etc.)
        processed_data = raw_data.dropna()  # Example of data cleaning
        processed_data = processed_data.drop_duplicates()  # Example of data cleaning

        # Step 3: Create Silver bucket key (path) to upload the processed Parquet data
        silver_key = f"processed/structured/{file_path.split('/')[-1].replace('.parquet', '_processed.parquet')}"

        # Step 4: Convert the processed data to Parquet format and upload to Silver bucket
        # Convert processed dataframe to Parquet
        table = pa.Table.from_pandas(processed_data)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)

        # Step 5: Upload processed Parquet data to Silver bucket
        s3.put_object(Bucket=f"{bucket_name}-silver-bucket", Key=silver_key, Body=parquet_buffer.getvalue())

        print(f"File successfully uploaded to Silver bucket: {bucket_name}-silver-bucket/{silver_key}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Simulate a file path and bucket name
    file_path = "raw/api_data/2025-03-15/transactions.parquet"  # Example file path in Bronze bucket (no s3:// prefix)
    bucket_name = "final-project"  # Your actual bucket name without "-silver"

    # Simulate processing and uploading to Silver
    process_and_upload_parquet(file_path, bucket_name)
