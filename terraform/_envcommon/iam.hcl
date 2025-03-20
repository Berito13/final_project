# terraform/_envcommon/iam.hcl

terraform {
  source = "${dirname(find_in_parent_folders())}//modules/iam"
}

# საერთო ცვლადები IAM მოდულისთვის
inputs = {
  common_tags = {
    ManagedBy = "Terragrunt"
  }
}