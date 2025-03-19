variable "lambda_function_name" {
  description = "Lambda ფუნქციის სახელი"
  type        = string
}

variable "lambda_role_arn" {
  description = "Lambda ფუნქციის IAM როლის ARN"
  type        = string
}

variable "source_bucket" {
  description = "Source S3 bucket"
  type        = string
}

variable "destination_bucket" {
  description = "Destination S3 bucket"
  type        = string
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

variable "pandas_layer_arn" {
  description = "ARN for AWS SDK Pandas Layer for Python 3.9"
  type        = string
  default     = "arn:aws:lambda:us-east-1:336392948345:layer:AWSSDKPandas-Python39:28"
}