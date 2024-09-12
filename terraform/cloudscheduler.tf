resource "google_project_service" "cloudscheduler" {
  service = "cloudscheduler.googleapis.com"

  disable_on_destroy = false
}

resource "google_cloud_scheduler_job" "default" {
  name             = "ping-invoice"
  region           = local.region
  schedule         = "* * * * *"
  time_zone        = "Etc/UTC"
  attempt_deadline = "30s"

  retry_config {
    retry_count = 1
  }

  http_target {
    http_method = "GET"
    uri         = "https://${google_api_gateway_gateway.default.default_hostname}/v1/health/invoice"
  }
}
