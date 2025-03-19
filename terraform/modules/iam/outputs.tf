# iam/output.tf

output "lambda_role_arn" {
  description = "Lambda ფუნქციის როლის ARN"
  value       = aws_iam_role.lambda_role.arn
}

output "lambda_role_name" {
  description = "Lambda ფუნქციის როლის სახელი"
  value       = aws_iam_role.lambda_role.name
}