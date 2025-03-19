# iam/variables.tf

variable "source_bucket" {
  description = "Source S3 bucket name (final-project-bronze-bucket)"
  type        = string
  default     = "final-project-bronze-bucket"
}

variable "destination_bucket" {
  description = "Destination S3 bucket name (final-project-silver-bucket)"
  type        = string
  default     = "final-project-silver-bucket"
}

variable "tags" {
  description = "Tags for IAM resources"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}