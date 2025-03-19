aws_region     = "us-east-1"
s3_bucket_names = ["lasha1", "lasha2", "lasha3"]
environments   = ["Dev", "Staging", "Production"]
enable_versioning = true
tags = {
  ManagedBy = "Terraform"
  Owner     = "Lasha"
  Project   = "Demo"
}