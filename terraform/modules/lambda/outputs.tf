output "lambda_function_arn" {
  description = "Lambda ფუნქციის ARN"
  value       = aws_lambda_function.lambda.arn
}

output "lambda_function_name" {
  description = "Lambda ფუნქციის სახელი"
  value       = aws_lambda_function.lambda.function_name
}
