# terraform/dev/s3/terragrunt.hcl

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${dirname(find_in_parent_folders())}/_envcommon/s3.hcl"
}

# dev გარემოს s3-სპეციფიკური ცვლადები
inputs = {
  bucket_name_prefix = "dev-my-project"
  versioning_enabled = true

  cors_rule = {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "PUT", "POST"]
    allowed_origins = ["https://dev.example.com"]
    max_age_seconds = 3000
  }

  lifecycle_rules = [
    {
      id      = "dev-rule"
      enabled = true
      prefix  = "logs/"

      expiration = {
        days = 30
      }
    }
  ]

  tags = {
    Environment = "dev"
    Project     = "my-project"
  }
}