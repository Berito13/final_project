# terraform/prod/terragrunt.hcl

include {
  path = find_in_parent_folders()
}

# prod გარემოს სპეციფიკური ცვლადები
inputs = {
  environment = "prod"
  # სხვა prod-სპეციფიკური ცვლადები
}