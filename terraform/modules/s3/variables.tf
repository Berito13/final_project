variable "bucket_names" {
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

variable "tags" {
  description = "ტეგები ყველა bucket-ისთვის"
  type        = map(string)
  default     = {
    ManagedBy = "Terraform"
    Owner     = "Lasha"
  }
}