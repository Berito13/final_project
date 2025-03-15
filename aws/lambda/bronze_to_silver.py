import boto3
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa
from io import BytesIO

# AWS client initialization
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get bucket name and file path from the event
        bucket_name = event.get('bucket_name', 'final-project')
        file_path = event.get('file_path', 'raw/api_data/2025-03-15/transactions.parquet')

        # Step 1: Download the raw Parquet file from the Bronze bucket
        print(f"Downloading file from S3 bucket: {bucket_name}-bronze-bucket/{file_path}")

        response = s3.get_object(Bucket=f"{bucket_name}-bronze-bucket", Key=file_path)
        file_content = response['Body'].read()

        # Create a BytesIO object to simulate a file object
        parquet_buffer = BytesIO(file_content)

        # Read the parquet file using pandas
        raw_data = pd.read_parquet(parquet_buffer)

        # Step 2: Process data
        processed_data = raw_data.dropna()
        processed_data = processed_data.drop_duplicates()

        # Step 3: Create Silver bucket key
        silver_key = f"processed/structured/{file_path.split('/')[-1].replace('.parquet', '_processed.parquet')}"

        # Step 4: Convert to Parquet format
        table = pa.Table.from_pandas(processed_data)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)

        # Step 5: Upload to Silver bucket
        s3.put_object(Bucket=f"{bucket_name}-silver-bucket", Key=silver_key, Body=parquet_buffer.getvalue())

        print(f"File successfully uploaded to Silver bucket: {bucket_name}-silver-bucket/{silver_key}")

        return {
            'statusCode': 200,
            'body': f"Successfully processed {file_path} and uploaded to {silver_key}"
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': f"Error processing file: {str(e)}"
        }

if __name__ == "__main__":
    # Example event data simulating the trigger event in Lambda
    event = {
        'bucket_name': 'final-project',  # Your actual bucket name without "-silver"
        'file_path': 'raw/api_data/2025-03-15/transactions.parquet'  # Sample file path from the Bronze bucket
    }
    # context can be simulated as None for local testing
    context = None

    response = lambda_handler(event, context)
    print(response)
