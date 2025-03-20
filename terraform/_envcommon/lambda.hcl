# terraform/_envcommon/lambda.hcl

terraform {
  source = "${dirname(find_in_parent_folders())}//modules/lambda"
}

# Lambda მოდულის საერთო ცვლადები
inputs = {
  runtime     = "nodejs18.x"
  common_tags = {
    ManagedBy = "Terragrunt"
  }
}