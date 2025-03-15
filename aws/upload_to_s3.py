import boto3
import logging
import os
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# AWS credentials from environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)


class S3DataLake:
    def __init__(self, project_name):
        """Initialize the S3 Data Lake"""
        self.project_name = project_name
        self.bronze_bucket = f"{project_name}-bronze-bucket"
        self.silver_bucket = f"{project_name}-silver-bucket"
        self.gold_bucket = f"{project_name}-gold-bucket"
        self.s3_client = s3_client  # Use already initialized s3_client

    def create_buckets(self):
        """Create the bronze, silver, and gold S3 buckets if they don't exist"""
        buckets = [self.bronze_bucket, self.silver_bucket, self.gold_bucket]

        # Get current region
        region = self.s3_client.meta._client_config.region_name
        logger.info(f"Using AWS region: {region}")

        # Get existing buckets
        existing_buckets = [bucket['Name'] for bucket in self.s3_client.list_buckets()['Buckets']]
        logger.info(f"Existing buckets: {existing_buckets}")

        # Create buckets if they don't exist
        for bucket in buckets:
            if bucket not in existing_buckets:
                try:
                    create_bucket_params = {"Bucket": bucket}

                    # For 'us-east-1', don't add LocationConstraint at all
                    if region != 'us-east-1':
                        create_bucket_params["CreateBucketConfiguration"] = {"LocationConstraint": region}

                    logger.info(f"Creating bucket {bucket} with params: {create_bucket_params}")

                    # Create the bucket (no LocationConstraint for us-east-1)
                    self.s3_client.create_bucket(**create_bucket_params)

                    logger.info(f"Created bucket: {bucket}")

                    # Wait for the bucket to be created and become available
                    waiter = self.s3_client.get_waiter('bucket_exists')
                    waiter.wait(Bucket=bucket)
                    logger.info(f"Bucket {bucket} is now available.")

                except Exception as e:
                    # Log more detailed information about the exception
                    logger.error(f"Error creating bucket {bucket}: {str(e)}", exc_info=True)
                    logger.error(
                        f"Failed to create bucket: {bucket} - Please check if there are any permission issues or conflicting resources.")
            else:
                logger.info(f"Bucket already exists: {bucket}")

        return buckets

    def create_folder_structure(self):
        """Create the folder structure in the S3 buckets"""
        bronze_prefixes = [
            "raw/api_data/",
            "raw/database_exports/",
            "raw/file_uploads/",
            "raw/streaming_data/",
            "archive/"
        ]

        silver_prefixes = [
            "processed/structured/",
            "processed/validated/",
            "processed/enriched/",
            "rejected/"
        ]

        gold_prefixes = [
            "analytics/kpi_metrics/",
            "analytics/ml_features/",
            "reporting/daily/",
            "reporting/weekly/",
            "reporting/monthly/",
            "dashboards/"
        ]

        for prefix in bronze_prefixes:
            self.s3_client.put_object(Bucket=self.bronze_bucket, Key=prefix)

        for prefix in silver_prefixes:
            self.s3_client.put_object(Bucket=self.silver_bucket, Key=prefix)

        for prefix in gold_prefixes:
            self.s3_client.put_object(Bucket=self.gold_bucket, Key=prefix)

        logger.info("Created folder structure in all buckets")

    def upload_sample_data(self, local_file_path, source_type):
        """Upload sample data to bronze layer"""
        try:
            current_date = datetime.now().strftime("%Y-%m-%d")
            bronze_key = f"raw/{source_type}/{current_date}/{os.path.basename(local_file_path)}"
            self.s3_client.upload_file(local_file_path, self.bronze_bucket, bronze_key)
            logger.info(f"Uploaded {local_file_path} to s3://{self.bronze_bucket}/{bronze_key}")
            return bronze_key
        except Exception as e:
            logger.error(f"Error uploading to Bronze layer: {str(e)}")
            return None

    def get_bucket_info(self):
        """Return information about the data lake buckets"""
        return {
            "project_name": self.project_name,
            "bronze_bucket": self.bronze_bucket,
            "silver_bucket": self.silver_bucket,
            "gold_bucket": self.gold_bucket
        }


def main():
    project_name = "final-project"
    data_lake = S3DataLake(project_name)

    # Create buckets
    data_lake.create_buckets()

    # Create folder structure
    data_lake.create_folder_structure()

    # Upload the sample file
    data_lake.upload_sample_data(
        r'C:\Users\Administrator\PycharmProjects\final_project\data\sample\transactions.parquet', 'api_data')

    # Display data lake info
    lake_info = data_lake.get_bucket_info()
    logger.info(f"Data Lake created with buckets: {lake_info}")

    logger.info("S3 Data Lake setup completed successfully")


if __name__ == "__main__":
    main()
