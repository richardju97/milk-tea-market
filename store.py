# store.py
# Handles store objects for each player

class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)
        self.totalrevenue = 0
        self.dailyrevenue = 0
        self.opDays = 0

# need inventory attributes

    def getName(self):
        return self.name

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
        self.opDays += 1

    def getTotalRevenue(self):
        return self.totalrevenue

    def getOpDays(self):
        return self.opDays
