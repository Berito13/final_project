# terraform/dev/terragrunt.hcl

include {
  path = find_in_parent_folders()
}

# dev გარემოს სპეციფიკური ცვლადები
inputs = {
  environment = "dev"
  # სხვა dev-სპეციფიკური ცვლადები
}