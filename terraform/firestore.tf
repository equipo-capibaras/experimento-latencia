resource "google_project_service" "firestore" {
  service = "firestore.googleapis.com"

  disable_on_destroy = false
}


resource "google_firestore_database" "default" {
  name                    = local.database_name
  location_id             = local.region
  type                    = "FIRESTORE_NATIVE"
  deletion_policy         = "DELETE"
  delete_protection_state = "DELETE_PROTECTION_ENABLED"

  depends_on = [ google_project_service.firestore ]
}
