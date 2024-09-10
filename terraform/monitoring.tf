resource "google_project_service" "cloudtrace" {
  service = "cloudtrace.googleapis.com"

  disable_on_destroy = false
}
