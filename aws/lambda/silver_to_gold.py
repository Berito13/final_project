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
        file_path = event.get('file_path', 'processed/structured/transactions_processed.parquet')

        # Step 1: Download the processed Parquet file from the Silver bucket
        print(f"Downloading file from S3 bucket: {bucket_name}-silver-bucket/{file_path}")

        response = s3.get_object(Bucket=f"{bucket_name}-silver-bucket", Key=file_path)
        file_content = response['Body'].read()

        # Create a BytesIO object to simulate a file object
        parquet_buffer = BytesIO(file_content)

        # Read the parquet file using pandas
        raw_data = pd.read_parquet(parquet_buffer)

        # Step 2: Apply final transformations (e.g., aggregating, renaming columns, etc.)
        # Example: Here we can do aggregations, or add any business logic
        if 'amount' in raw_data.columns:
            raw_data['total_amount'] = raw_data['amount'] * 1.1  # Example of a simple transformation

        # Step 3: Create Gold bucket key
        gold_key = f"aggregated/business_ready/{file_path.split('/')[-1].replace('_processed', '_gold')}"

        # Step 4: Convert to Parquet format
        table = pa.Table.from_pandas(raw_data)
        parquet_buffer = BytesIO()
        pq.write_table(table, parquet_buffer)
        parquet_buffer.seek(0)

        # Step 5: Upload to Gold bucket
        s3.put_object(Bucket=f"{bucket_name}-gold-bucket", Key=gold_key, Body=parquet_buffer.getvalue())

        print(f"File successfully uploaded to Gold bucket: {bucket_name}-gold-bucket/{gold_key}")

        return {
            'statusCode': 200,
            'body': f"Successfully processed {file_path} and uploaded to {gold_key}"
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
        'bucket_name': 'final-project',  # Your actual bucket name without "-gold"
        'file_path': 'processed/structured/transactions_processed.parquet'  # Sample file path from the Silver bucket
    }
    # context can be simulated as None for local testing
    context = None

    response = lambda_handler(event, context)
    print(response)
