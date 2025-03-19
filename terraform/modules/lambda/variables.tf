# lambda/variables.tf

variable "lambda_function_name" {
  description = "Lambda ფუნქციის სახელი"
  type        = string
  default     = "bronze_to_silver_processor"
}

variable "lambda_role_arn" {
  description = "Lambda ფუნქციის IAM როლის ARN"
  type        = string
}

variable "source_bucket" {
  description = "Source S3 bucket (exam-bronze)"
  type        = string
  default     = "exam-bronze"
}

variable "destination_bucket" {
  description = "Destination S3 bucket (exam-silver)"
  type        = string
  default     = "exam-silver"
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
  description = "Tags for Lambda resources"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}