# Experimento Latencia

# Setup
1. Create a new project in GCP
2. Enable the following APIs for managing resources with terraform
- https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview
- https://console.developers.google.com/apis/api/serviceusage.googleapis.com/overview
3. Create GCP bucket to store terraform state
4. Go to folder `terraform` and run the following command to initialize terraform
```sh
terraform init -backend-config "bucket=<name of bucket used to store terraform state>"
```
5. Create infrastructure using terraform with
```sh
terraform apply -var "gcp_project_id=<gcp project name>"
```
