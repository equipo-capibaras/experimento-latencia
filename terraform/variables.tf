variable "gcp_region" {
  type        = string
  default     = "us-central1"
  description = "GCP region"
}

variable "gcp_project_id" {
  type        = string
  description = "GCP project ID"
}

variable "registry_id" {
  type        = string
  default     = "repo"
  description = "Artifact registry ID"
}

variable "service_name" {
  type        = string
  default     = "invoice"
  description = "Microservice name"
}

variable "database_name" {
  type        = string
  default     = "invoicedb"
  description = "Firestore database name"
}

variable "api_id" {
  type        = string
  default     = "exp-latency"
  description = "API Gateway API ID"
}
