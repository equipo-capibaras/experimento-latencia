from flask import Blueprint, Response, current_app, request, g
from flask.views import MethodView
from repositories import InvoiceRepository
from .util import class_route
from gcp import TraceSpan, TraceFunction

blp = Blueprint("Invoice", __name__)

@class_route(blp, "/<id>")
class InvoiceView(MethodView):
    init_every_request = False

    @TraceFunction("Get invoice")
    def get(self, id):
        invoice_repository = current_app.repositories[InvoiceRepository]

        invoice = invoice_repository.get_invoice(id)
        
        resp = Response(f"Invoice: {invoice}\n\nHeaders:\n{request.headers}", status=200, mimetype='text/plain')

        return resp
