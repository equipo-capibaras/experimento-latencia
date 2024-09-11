from flask import Flask
from blueprints import BlueprintHealth, BlueprintInvoice
from repositories import InvoiceRepository
from repositories.firestore import FirestoreInvoiceRepository
from gcp import setup_cloud_logging, setup_cloud_trace, setup_apigateway

API_PREFIX = "/v1/invoices"

def create_app():
    setup_cloud_logging()

    app = Flask(__name__)

    setup_cloud_trace(app)
    setup_apigateway(app)

    app.repositories = {InvoiceRepository: FirestoreInvoiceRepository()}

    app.register_blueprint(BlueprintHealth)
    app.register_blueprint(BlueprintInvoice, url_prefix=API_PREFIX)

    return app
