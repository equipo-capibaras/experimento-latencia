from flask import Blueprint, Response, current_app
from flask.views import MethodView
from repositories import InvoiceRepository
from .util import class_route

blp = Blueprint("Invoice", __name__)

@class_route(blp, "/<id>")
class InvoiceView(MethodView):
    init_every_request = False

    def get(self, id):
        invoice_repository = current_app.repositories[InvoiceRepository]

        invoice = invoice_repository.get_invoice(id)

        return Response(f"Invoice: {invoice}", status=200, mimetype='text/plain')
