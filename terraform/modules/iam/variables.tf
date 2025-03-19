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
variable "s3_bucket_names" {
  description = "S3 bucket-ების სახელების სია"
  type        = list(string)
  default     = ["final-project-bronze-bucket", "final-project-silver-bucket", "final-project-gold-bucket"]
}

variable "tags" {
  description = "Tags for IAM resources"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}

variable "lambda_role_arn" {
  description = "Lambda ფუნქციის IAM როლის ARN"
  type        = string
  default     = ""  # თუნდაც შეიქმნას და გამოიქცეს, ჩვენ ეს ვერ გამოვიყენებთ, რადგან IAM როლი უშუალოდ აისახება output-ში
}