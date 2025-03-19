# lambda/main.tf

# Lambda ფუნქციის zip ფაილის შექმნა
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/src/${var.lambda_function_name}.py"
  output_path = "${path.module}/files/${var.lambda_function_name}.zip"
}

# Lambda ფუნქციის შექმნა
resource "aws_lambda_function" "lambda" {
  filename         = data.archive_file.lambda_zip.output_path
  function_name    = var.lambda_function_name
  role             = var.lambda_role_arn
  handler          = "${var.lambda_function_name}.lambda_handler"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256
  runtime          = "python3.9"
  timeout          = 60
  memory_size      = 128

  environment {
    variables = {
      SOURCE_BUCKET      = var.source_bucket
      DESTINATION_BUCKET = var.destination_bucket
    }
  }

  tags = var.tags
}

# S3 ევენთის ტრიგერის კონფიგურაცია
resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3Bucket-${var.lambda_function_name}"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.arn
  principal     = "s3.amazonaws.com"
  source_arn    = "arn:aws:s3:::${var.source_bucket}"
}

# S3 ბაკეტის ნოთიფიკაციის კონფიგურაცია
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = var.source_bucket

  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = var.s3_filter_prefix
    filter_suffix       = var.s3_filter_suffix
  }

  depends_on = [aws_lambda_permission.allow_s3]
}