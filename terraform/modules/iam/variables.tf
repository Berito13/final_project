# iam/variables.tf

variable "source_bucket" {
  description = "Source S3 bucket name (lasha1)"
  type        = string
  default     = "lasha1"
}

variable "destination_bucket" {
  description = "Destination S3 bucket name (lasha2)"
  type        = string
  default     = "lasha2"
}

variable "tags" {
  description = "Tags for IAM resources"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}