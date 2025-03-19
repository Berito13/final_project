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

module "lambda_bronze_to_silver" {
  source = "./modules/lambda"

  lambda_function_name = var.lambda_function_name_bronze_to_silver  # Lambda ფუნქციის სახელი
  lambda_role_arn      = module.iam.lambda_role_arn  # IAM როლის ARN
  source_bucket        = var.s3_bucket_names[0]  # source bucket
  destination_bucket   = var.s3_bucket_names[1]  # destination bucket
  tags                 = var.tags

  s3_filter_prefix     = ""  # ცარიელი ნიშნავს ყველა ფაილს
  s3_filter_suffix     = ""  # მაგ: ".csv" თუ მხოლოდ CSV ფაილები გჭირდებათ

  depends_on = [module.s3, module.iam]
}

module "lambda_silver_to_gold" {
  source = "./modules/lambda"

  lambda_function_name = var.lambda_function_name_silver_to_gold  # Lambda ფუნქციის სახელი
  lambda_role_arn      = module.iam.lambda_role_arn  # IAM როლის ARN
  source_bucket        = var.s3_bucket_names[1]  # source bucket
  destination_bucket   = var.s3_bucket_names[2]  # destination bucket
  tags                 = var.tags

  s3_filter_prefix     = ""  # ცარიელი ნიშნავს ყველა ფაილს
  s3_filter_suffix     = ""  # მაგ: ".csv" თუ მხოლოდ CSV ფაილები გჭირდებათ

  depends_on = [module.s3, module.iam]
}
