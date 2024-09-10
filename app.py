import os
from flask import Flask
from blueprints import BlueprintHealth, BlueprintInvoice
from repositories import InvoiceRepository
from repositories.firestore import FirestoreInvoiceRepository
from gcp import setup_cloud_logging

API_PREFIX = "/v1/invoices"

def create_app():
    if os.getenv('ENABLE_CLOUD_LOGGING') == '1':
        setup_cloud_logging()

    app = Flask(__name__)

    app.repositories = {InvoiceRepository: FirestoreInvoiceRepository()}

    app.register_blueprint(BlueprintHealth)
    app.register_blueprint(BlueprintInvoice, url_prefix=API_PREFIX)

    return app
