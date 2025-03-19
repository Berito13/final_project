# iam/variables.tf

variable "source_bucket" {
  description = "Source S3 bucket name (exam-bronze)"
  type        = string
  default     = "exam-bronze"
}

variable "destination_bucket" {
  description = "Destination S3 bucket name (exam-silver)"
  type        = string
  default     = "exam-silver"
}

variable "tags" {
  description = "Tags for IAM resources"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}