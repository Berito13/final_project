# S3 bucket-ების შექმნა
resource "aws_s3_bucket" "buckets" {
  count  = length(var.bucket_names)
  bucket = var.bucket_names[count.index]

  tags = merge(
    var.tags,
    {
      Name        = var.bucket_names[count.index]
      Environment = var.environments[count.index]
    }
  )
}

# ვერსიონირების კონფიგურაცია
resource "aws_s3_bucket_versioning" "bucket_versioning" {
  count  = var.enable_versioning ? length(var.bucket_names) : 0
  bucket = aws_s3_bucket.buckets[count.index].id

  versioning_configuration {
    status = "Enabled"
  }
}

# ენკრიპციის კონფიგურაცია
resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_encryption" {
  count  = length(var.bucket_names)
  bucket = aws_s3_bucket.buckets[count.index].id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# საჯარო წვდომის ბლოკირება
resource "aws_s3_bucket_public_access_block" "bucket_public_access_block" {
  count  = length(var.bucket_names)
  bucket = aws_s3_bucket.buckets[count.index].id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}