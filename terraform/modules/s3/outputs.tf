output "bucket_arns" {
  description = "შექმნილი S3 bucket-ების ARN-ები"
  value       = aws_s3_bucket.buckets[*].arn
}

output "bucket_names" {
  description = "შექმნილი S3 bucket-ების სახელები"
  value       = aws_s3_bucket.buckets[*].bucket
}

output "bucket_domain_names" {
  description = "შექმნილი S3 bucket-ების დომენური სახელები"
  value       = aws_s3_bucket.buckets[*].bucket_domain_name
}