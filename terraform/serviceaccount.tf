resource "google_project_service" "iam" {
  service = "iam.googleapis.com"

  disable_on_destroy = false
}

resource "google_service_account" "default" {
  account_id   = local.service_account_name
  display_name = "Service Account ${local.service_name}"

  depends_on = [ google_project_service.iam ]
}
