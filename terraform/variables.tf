variable "aws_region" {
  description = "AWS რეგიონი"
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_names" {
  description = "S3 bucket-ების სახელების სია"
  type        = list(string)
  default     = ["final-project-bronze-bucket", "final-project-silver-bucket", "final-project-gold-bucket"]
}

variable "environments" {
  description = "გარემოები თითოეული bucket-ისთვის"
  type        = list(string)
  default     = ["Dev", "Staging", "Production"]
}

variable "enable_versioning" {
  description = "ვერსიონირების ჩართვა bucket-ებზე"
  type        = bool
  default     = true
}

variable "lambda_function_name_bronze_to_silver" {
  description = "Bronze to Silver Lambda ფუნქციის სახელი"
  type        = string
  default     = "bronze_to_silver_processor"  # ლამბდა სახელი, რომელიც ავტომატურად დაისახება
}

variable "lambda_function_name_silver_to_gold" {
  description = "Silver to Gold Lambda ფუნქციის სახელი"
  type        = string
  default     = "silver_to_gold_processor"  # ლამბდა სახელი, რომელიც ავტომატურად დაისახება
}

variable "lambda_role_arn" {
  description = "Lambda ფუნქციის IAM როლის ARN"
  type        = string
  default     = "arn:aws:iam::987654321098:role/s3_processing_lambda_role"  # თქვენი ARN
}

variable "source_bucket" {
  description = "Source S3 bucket"
  type        = string
  default     = "final-project-bronze-bucket"  # ეს უკვე გაქვს დეფოლტად
}

variable "destination_bucket" {
  description = "Destination S3 bucket"
  type        = string
  default     = "final-project-silver-bucket"  # ეს უკვე გაქვს დეფოლტად
}

variable "s3_filter_prefix" {
  description = "S3 ნოთიფიკაციის ფილტრი (prefix)"
  type        = string
  default     = ""  # ცარიელი ნიშნავს ყველა ობიექტს
}

variable "s3_filter_suffix" {
  description = "S3 ნოთიფიკაციის ფილტრი (suffix), მაგ: .csv, .json"
  type        = string
  default     = ""  # ცარიელი ნიშნავს ყველა ობიექტს
}

variable "tags" {
  description = "ტეგები ყველა bucket-ისთვის"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
    Project   = "Demo"
  }
}
