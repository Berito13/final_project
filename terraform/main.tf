# AWS პროვაიდერის კონფიგურაცია
provider "aws" {
  region = var.aws_region
}

# S3 მოდულის გამოძახება
module "s3" {
  source = "./modules/s3"

  bucket_names      = var.s3_bucket_names
  environments      = var.environments
  enable_versioning = var.enable_versioning
  tags              = var.tags
}