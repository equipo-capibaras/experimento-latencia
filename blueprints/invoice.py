import json
from flask import Blueprint, Response, current_app, request, g
from flask.views import MethodView
from repositories import InvoiceRepository
from .util import class_route, requires_token
from gcp import TraceSpan, TraceFunction

blp = Blueprint("Invoice", __name__)

def _combine_dicts(a, b):
    common_keys = set(a.keys()) & set(b.keys())
    result = {key: {'a': a[key], 'b': b[key]} for key in common_keys}
    return result

@class_route(blp, "/<id>")
class InvoiceView(MethodView):
    init_every_request = False

    @requires_token
    @TraceFunction("Get invoice")
    def get(self, id):
        invoice_repository = current_app.repositories[InvoiceRepository]

        client_id = g.user_token['cid']
        invoice = invoice_repository.get_invoice(client_id, id)
        
        if not invoice:
            return Response(json.dumps({'message': f'Invoice {id} not found', 'code': 404}), status=404, mimetype='application/json')

        incident_dict = {
            key: {
                'count': invoice.incidents[key],
                'rate': invoice.rate.perIncident[key],
                'total': invoice.incidents[key] * invoice.rate.perIncident[key],
            } for key in invoice.incidents.keys()
        }
        cost_total = sum([x['total'] for x in incident_dict.values()])

        resp_dict = {
            'dateGeneration': invoice.dateGeneration.isoformat(),
            'datePayment': invoice.datePayment.isoformat(),
            'datePaymentLimit': invoice.datePaymentLimit.isoformat(),
            'incidents': incident_dict,
            'total': cost_total
        }

        return Response(json.dumps(resp_dict), status=200, mimetype='application/json')
