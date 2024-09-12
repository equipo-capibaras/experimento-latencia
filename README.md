# Experimento Latencia

## Project Structure Overview
This Flask application adheres to a structured layout that promotes separation of concerns and maintainability.

- blueprints/: This folder houses Blueprints, which represent modular components of the presentation layer.
- models/: Defines the data models, such as Invoice, that represent the structure of data used within the application.
- repositories/: Contains repository classes, such as FirestoreInvoiceRepository, responsible for interacting with data storage (e.g., Firestore).
- gcp/: Contains code specific to the Google Cloud Platform (GCP), allowing for seamless integration with GCP services.
- terraform/: Stores Terraform configuration files, enabling infrastructure-as-code deployment and management on GCP.
- app.py: The core of the application, this file initializes the Flask app.
- Dockerfile: Defines the instructions for building a Docker image of the application.
- requirements.txt: Lists the project's dependencies, making it easy to recreate the development environment.
- README.md: This file (you're reading it!) provides an overview of the project structure and other essential information.

## Setup
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
6. Go to project root and build container image with
```sh
docker build -t us-central1-docker.pkg.dev/<gcp project name>/repo/test:b1 .
```
7. Push container image to registry with
```sh
docker push us-central1-docker.pkg.dev/<gcp project name>/repo/test:b1
```
8. Deploy container image to Cloud Run with
```sh
gcloud run deploy invoice --region us-central1 --image=us-central1-docker.pkg.dev/<gcp project name>/repo/test:b7
```

**Note:** After all tests have been completed, the entire infrastructure can be destroyed with:
```sh
terraform destroy -var "gcp_project_id=<gcp project name>"
```
