aws_region     = "us-east-1"
s3_bucket_names = ["final-project-bronze-bucket", "final-project-silver-bucket", "final-project-gold-bucket"]
environments   = ["Dev", "Staging", "Production"]
enable_versioning = true
tags = {
  ManagedBy = "Terraform"
  Owner     = "Lasha"
  Project   = "Demo"
}