# terraform/dev/lambda/terragrunt.hcl

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

# dev გარემოს lambda-სპეციფიკური ცვლადები
inputs = {
  function_name = "dev-lambda-function"
  handler       = "index.handler"
  runtime       = "nodejs18.x"
  memory_size   = 128
  timeout       = 30

  # IAM როლის ARN მიღება დამოკიდებული მოდულიდან
  role_arn      = dependency.iam.outputs.lambda_role_arn

  environment_variables = {
    ENV_TYPE = "development"
    LOG_LEVEL = "DEBUG"
  }

  tags = {
    Environment = "dev"
    Project     = "my-project"
  }
}