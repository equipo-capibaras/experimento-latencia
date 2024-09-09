terraform {
  required_providers {
    google = {
      version = "~> 6.1.0"
    }

    google-beta = {
      version = "~> 6.1.0"
    }
  }
}

terraform {
  backend "gcs" {
    prefix = "exp-latencia/state"
  }
}

provider "google" {
  project = local.project_id
  region  = local.region
}

provider "google-beta" {
  project = local.project_id
  region  = local.region
}
