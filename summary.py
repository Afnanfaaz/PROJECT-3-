class DataSummary:
    def __init__(self, data):
        self.data = data

    def summary(self):
        return self.data.describe(include='all')