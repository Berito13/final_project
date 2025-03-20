# terraform/_envcommon/s3.hcl

terraform {
  source = "${dirname(find_in_parent_folders())}//modules/s3"
}

# S3 მოდულის საერთო ცვლადები
inputs = {
  versioning = true
  common_tags = {
    ManagedBy = "Terragrunt"
  }
}