class Invoice:
    def __init__(self, id, dateGeneration, datePayment, datePaymentLimit, incidents, rate):
        self.id = id
        self.dateGeneration = dateGeneration
        self.datePayment = datePayment
        self.datePaymentLimit = datePaymentLimit
        self.incidents = incidents
        self.rate = rate

    def __str__(self):
        return f"ID: {self.id}\nDate of Generation: {self.dateGeneration}\nDate of Payment: {self.datePayment}\nPayment Due Date: {self.datePaymentLimit}\nIncidents: {self.incidents}\nRate: {self.rate}"
