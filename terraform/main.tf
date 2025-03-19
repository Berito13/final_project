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

# IAM მოდულის გამოძახება
module "iam" {
  source = "./modules/iam"

  source_bucket      = var.s3_bucket_names[0]      # lasha1
  destination_bucket = var.s3_bucket_names[1]      # lasha2
  tags               = var.tags
}

# Lambda მოდულის გამოძახება
module "lambda" {
  source = "./modules/lambda"

  lambda_role_arn    = module.iam.lambda_role_arn
  source_bucket      = var.s3_bucket_names[0]      # lasha1
  destination_bucket = var.s3_bucket_names[1]      # lasha2
  tags               = var.tags

  # შეგიძლიათ შეცვალოთ ეს ცვლადები საჭიროებისამებრ
  s3_filter_prefix   = ""  # ცარიელი ნიშნავს ყველა ფაილს
  s3_filter_suffix   = ""  # მაგ: ".csv" თუ მხოლოდ CSV ფაილები გჭირდებათ

  depends_on = [module.s3, module.iam]
}