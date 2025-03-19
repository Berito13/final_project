aws_region     = "us-east-1"
s3_bucket_names = ["exam-bronze", "exam-silver", "exam-gold"]
environments   = ["Dev", "Staging", "Production"]
enable_versioning = true
tags = {
  ManagedBy = "Terraform"
  Owner     = "Lasha"
  Project   = "Demo"
}