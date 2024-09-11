import logging
from google.cloud import firestore
from .. import InvoiceRepository
from models import Invoice, Rate
from gcp import TraceFunction

class FirestoreInvoiceRepository(InvoiceRepository):
    def __init__(self):
        self.db = firestore.Client(database='invoicedb')
        self.logger = logging.getLogger(self.__class__.__name__)

    @TraceFunction("Fetch invoice from DB")
    def get_invoice(self, client_id, invoice_id):
        doc_ref = self.db.collection('clients').document(client_id).collection('invoices').document(invoice_id)
        doc = doc_ref.get()
        if not doc.exists:
            return None

        doc_dict = doc.to_dict()

        rate = doc_dict['rate'].get()
        if not rate.exists:
            self.logger.error(f'Rate {doc_dict["rate"].id} of invoice {invoice_id} for client {client_id} not found')
            return None

        rate_dict = rate.to_dict()
        rate_obj = Rate(
            id = rate.id,
            baseFee = rate_dict['baseFee'],
            perIncident = rate_dict['perIncident']
        )

        return Invoice(
            id = doc.id,
            dateGeneration = doc_dict['dateGeneration'],
            datePayment = doc_dict['datePayment'],
            datePaymentLimit = doc_dict['datePaymentLimit'],
            incidents = doc_dict['incidents'],
            rate = rate_obj
        )
