resource "google_project_service" "servicecontrol" {
  service = "servicecontrol.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "servicemanagement" {
  service = "servicemanagement.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "apigateway" {
  service = "apigateway.googleapis.com"

  disable_on_destroy = false
}

resource "google_api_gateway_api" "default" {
  provider = google-beta
  api_id = local.api_id

  depends_on = [
    google_project_service.apigateway,
    google_project_service.servicecontrol,
    google_project_service.servicemanagement
  ]
}
