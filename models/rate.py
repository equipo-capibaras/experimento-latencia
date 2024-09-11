class Rate:
    def __init__(self, id, baseFee, perIncident):
        self.id = id
        self.baseFee = baseFee
        self.perIncident = perIncident

    def __str__(self):
        return f"ID: {self.id}\nBase Fee: {self.baseFee}\nPer incident fees: {self.perIncident}"
