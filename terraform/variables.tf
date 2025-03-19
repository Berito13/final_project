variable "aws_region" {
  description = "AWS რეგიონი"
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_names" {
  description = "S3 bucket-ების სახელების სია"
  type        = list(string)
  default     = ["lasha1", "lasha2", "lasha3"]
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

variable "tags" {
  description = "ტეგები ყველა bucket-ისთვის"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
    Project   = "Demo"
  }
}