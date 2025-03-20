# terraform/prod/iam/terragrunt.hcl

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${dirname(find_in_parent_folders())}/_envcommon/iam.hcl"
}

# prod გარემოს IAM-სპეციფიკური ცვლადები
inputs = {
  role_name_prefix = "prod-role"
  policy_name_prefix = "prod-policy"
  max_session_duration = 7200

  # დამატებითი IAM სპეციფიკური ცვლადები
  tags = {
    Environment = "prod"
    Project     = "my-project"
  }
}