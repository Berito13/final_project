# IAM როლი Lambda ფუნქციისთვის
resource "aws_iam_role" "lambda_role" {
  name = "s3_processing_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  tags = var.tags
}

# IAM როლის ARN-ს გამოსაყენებლად

# პოლისი S3-სთან სამუშაოდ
resource "aws_iam_policy" "s3_access_policy" {
  name        = "s3_buckets_access_policy"
  description = "Allow Lambda to access specific S3 buckets"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket",
          "s3:DeleteObject"
        ]
        Effect   = "Allow"
        Resource = flatten([
          for bucket in var.s3_bucket_names : [
            "arn:aws:s3:::${bucket}",
            "arn:aws:s3:::${bucket}/*"
          ]
        ])
      },
      {
        Action = [
          "s3:PutObject"
        ]
        Effect   = "Allow"
        Resource = "arn:aws:s3:::${var.s3_bucket_names[2]}/*"  # gold bucket
      }
    ]
  })
}

# პოლისის მიბმა როლზე
resource "aws_iam_role_policy_attachment" "lambda_s3_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}

# CloudWatch Logs-ისთვის საჭირო პოლისის მიბმა
resource "aws_iam_role_policy_attachment" "lambda_logs_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
