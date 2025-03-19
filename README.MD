# მონაცემთა პაიპლაინის პროექტი

## პროექტის მიმოხილვა
ეს პროექტი წარმოადგენს მონაცემთა დამუშავების პაიპლაინს, რომელიც იყენებს AWS Lambda-ს მონაცემთა შეგროვებისთვის, SQLite-ს მონაცემთა შენახვისა და დამუშავებისთვის, და Terraform-ს ინფრასტრუქტურის მართვისთვის.

## პროექტის არქიტექტურა

პროექტი შედგება სამი ძირითადი კომპონენტისგან:
1. **AWS Lambda ფუნქციები** - მონაცემთა შეგროვება და S3-ში ატვირთვა
2. **SQLite პაიპლაინი** - მონაცემთა დამუშავება და ანალიზი სხვადასხვა დონეზე (bronze, silver, gold)
3. **Terraform კონფიგურაცია** - პროექტის ინფრასტრუქტურის ავტომატური შექმნა და მართვა

## პროექტის სტრუქტურა

```
final_project/
├── aws/
│   └── lambda/
│       ├── __init__.py
│       └── upload_to_s3.py
├── data/
│   └── sample/
│       ├── __init__.py
│       ├── data_warehouse.db
│       └── generate_data.py
├── sqlite_pipeline/
│   ├── __init__.py
│   ├── bronze_layer.py
│   ├── create_tables.py
│   ├── gold_layer.py
│   ├── main.py
│   └── silver_layer.py
└── terraform/
    ├── .terraform/
    ├── environments/
    ├── modules/
    ├── .terraform.lock.hcl
    ├── backend.tf
    ├── main.tf
    ├── outputs.tf
    ├── providers.tf
    ├── terraform.tfstate
    ├── terraform.tfstate.backup
    ├── terraform.tfvars
    └── tfplan
```

## კომპონენტების დეტალური აღწერა

### AWS Lambda

AWS Lambda ფუნქციები პასუხისმგებელია მონაცემთა შეგროვებასა და S3 საცავში ატვირთვაზე.

**ძირითადი ფაილები:**
- `upload_to_s3.py` - ფუნქცია, რომელიც ახორციელებს aws-ზე s3-buckets შექმნას მონაცემთა ატვირთვას S3 ბაკეტში

### მონაცემთა სტრუქტურა

პროექტი იყენებს სატესტო მონაცემებს დამუშავების პროცესის დემონსტრირებისთვის.

**ძირითადი ფაილები:**
- `data_warehouse.db` - SQLite მონაცემთა ბაზა
- `generate_data.py` - სკრიპტი სატესტო მონაცემების გენერირებისთვის

### SQLite პაიპლაინი

მონაცემთა დამუშავების პაიპლაინი იყენებს Medallion არქიტექტურას (Bronze, Silver, Gold დონეები).

**ძირითადი ფაილები:**
- `create_tables.py` - მონაცემთა ბაზის სტრუქტურის შექმნა
- `bronze_layer.py` - პირველადი მონაცემების დამუშავება
- `silver_layer.py` - გასუფთავებული და ტრანსფორმირებული მონაცემები
- `gold_layer.py` - ბიზნეს მეტრიკების შექმნა
- `main.py` - პაიპლაინის ორკესტრაცია

### Terraform ინფრასტრუქტურა

Terraform კონფიგურაცია ავტომატურად ქმნის და მართავს პროექტის ინფრასტრუქტურას.

**ძირითადი ფაილები:**
- `main.tf` - ძირითადი რესურსების კონფიგურაცია
- `backend.tf` - Terraform სახელმწიფოს შენახვის კონფიგურაცია
- `providers.tf` - პროვაიდერების კონფიგურაცია
- `outputs.tf` - გამომავალი ცვლადები
- `terraform.tfvars` - ცვლადების მნიშვნელობები

## ინსტალაცია და გაშვება

### წინაპირობები
- Python 3.8+
- AWS CLI (კონფიგურირებული)
- Terraform 1.0+

### ინსტალაცია

1. კლონირება:
   ```bash
   git clone [https://github.com/Berito13/final_project.git]
   cd final_project
   ```

2. Python დამოკიდებულებების ინსტალაცია:
   ```bash
   pip install -r requirements.txt
   ```

3. Terraform ინფრასტრუქტურის ინიციალიზაცია:
   ```bash
   cd terraform
   terraform init
   ```

### ინფრასტრუქტურის შექმნა

1. Terraform კონფიგურაციის შემოწმება:
   ```bash
   terraform plan -out=tfplan
   ```

2. ინფრასტრუქტურის შექმნა:
   ```bash
   terraform apply tfplan
   ```

### პაიპლაინის გაშვება

SQLite პაიპლაინის გაშვება:
```bash
cd sqlite_pipeline
python main.py
```

## გამოყენების მაგალითები

### მონაცემთა გენერირება

```python
python data/sample/generate_data.py
```

### მონაცემთა დამუშავება

```python
python sqlite_pipeline/main.py
```

## ავტორი

[ლაშა ბერიშვილი]
