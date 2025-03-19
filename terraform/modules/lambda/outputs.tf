# lambda/output.tf

output "lambda_function_arn" {
  description = "Lambda ფუნქციის ARN"
  value       = aws_lambda_function.bronze_to_silver.arn
}

output "lambda_function_name" {
  description = "Lambda ფუნქციის სახელი"
  value       = aws_lambda_function.bronze_to_silver.function_name
}

output "lambda_function_invoke_arn" {
  description = "Lambda ფუნქციის Invoke ARN"
  value       = aws_lambda_function.bronze_to_silver.invoke_arn
}