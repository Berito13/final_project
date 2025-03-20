# terraform/prod/s3/terragrunt.hcl

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${dirname(find_in_parent_folders())}/_envcommon/s3.hcl"
}

# prod გარემოს s3-სპეციფიკური ცვლადები
inputs = {
  bucket_name_prefix = "prod-my-project"
  versioning_enabled = true

  cors_rule = {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "PUT", "POST"]
    allowed_origins = ["https://www.example.com"]
    max_age_seconds = 3000
  }

  lifecycle_rules = [
    {
      id      = "prod-rule"
      enabled = true
      prefix  = "logs/"

      expiration = {
        days = 90
      }
    }
  ]

  tags = {
    Environment = "prod"
    Project     = "my-project"
  }
}