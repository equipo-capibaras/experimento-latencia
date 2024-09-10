from flask import Blueprint, Response, current_app, request
from flask.views import MethodView
from repositories import InvoiceRepository
from .util import class_route
from gcp import TraceSpan

blp = Blueprint("Invoice", __name__)

@class_route(blp, "/<id>")
class InvoiceView(MethodView):
    init_every_request = False

    def get(self, id):
        with TraceSpan("Get invoice"):
            invoice_repository = current_app.repositories[InvoiceRepository]

            with TraceSpan("Fetch invoice from DB"):
                invoice = invoice_repository.get_invoice(id)
            
            resp = Response(f"Invoice: {invoice}\n\nHeaders:\n{request.headers}", status=200, mimetype='text/plain')

        return resp
