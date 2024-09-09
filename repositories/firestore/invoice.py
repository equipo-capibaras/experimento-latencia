from google.cloud import firestore
from .. import InvoiceRepository

class FirestoreInvoiceRepository(InvoiceRepository):
    def __init__(self):
        self.db = firestore.Client(database='invoicedb')

    def get_invoice(self, id):
        doc_ref = self.db.collection('invoices').document(id)
        doc = doc_ref.get()
        if doc.exists:
            return Invoice(doc.id, doc.to_dict()['name'])
        else:
            return None
