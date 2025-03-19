output "s3_bucket_arns" {
  description = "შექმნილი S3 bucket-ების ARN-ები"
  value       = module.s3.bucket_arns
}

output "s3_bucket_names" {
  description = "შექმნილი S3 bucket-ების სახელები"
  value       = module.s3.bucket_names
}

output "s3_bucket_domain_names" {
  description = "შექმნილი S3 bucket-ების დომენური სახელები"
  value       = module.s3.bucket_domain_names
}