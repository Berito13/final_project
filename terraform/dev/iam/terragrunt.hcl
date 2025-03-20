# terraform/dev/iam/terragrunt.hcl

include "root" {
  path = find_in_parent_folders()
}

include "envcommon" {
  path = "${dirname(find_in_parent_folders())}/_envcommon/iam.hcl"
}

# dev გარემოს IAM-სპეციფიკური ცვლადები
inputs = {
  role_name_prefix = "dev-role"
  policy_name_prefix = "dev-policy"
  max_session_duration = 3600

  # დამატებითი IAM სპეციფიკური ცვლადები
  tags = {
    Environment = "dev"
    Project     = "my-project"
  }
}