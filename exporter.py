import pandas as pd

class Exporter:
    def __init__(self, data):
        self.data = data

    def to_csv(self):
        for table, df in self.data.items():
            df.to_csv(f"{table}.csv", index=False)
