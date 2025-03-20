# terraform/prod/lambda/terragrunt.hcl

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${dirname(find_in_parent_folders())}/_envcommon/lambda.hcl"
}

# დამოკიდებულება IAM მოდულზე
dependency "iam" {
  config_path = "../iam"
}

# prod გარემოს lambda-სპეციფიკური ცვლადები
inputs = {
  function_name = "prod-lambda-function"
  handler       = "index.handler"
  runtime       = "nodejs18.x"
  memory_size   = 256
  timeout       = 60

  # IAM როლის ARN მიღება დამოკიდებული მოდულიდან
  role_arn      = dependency.iam.outputs.lambda_role_arn

  environment_variables = {
    ENV_TYPE = "production"
    LOG_LEVEL = "INFO"
  }

  tags = {
    Environment = "prod"
    Project     = "my-project"
  }
}