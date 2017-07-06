# store.py
# Handles store objects for each player

class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.totalrevenue = 0
        self.dailyrevenue = 0

    def changePrice(self, price):
        self.price = price

    def processSale(self):
        self.dailyrevenue += self.price

    def aggregateRevenue(self):
        self.totalrevenue += self.dailyrevenue
        self.dailyrevenue = 0
