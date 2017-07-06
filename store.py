# store.py
# Handles store objects for each player

class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)
        self.totalrevenue = 0
        self.dailyrevenue = 0

    def getPrice(self):
        return self.price

    def changePrice(self, price):
        self.price = int(price)

    def processSale(self):
        self.dailyrevenue += self.price

    def getDailyRevenue(self):
        return self.dailyrevenue

    def aggregateRevenue(self):
        self.totalrevenue += self.dailyrevenue
        self.dailyrevenue = 0
