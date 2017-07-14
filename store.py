# store.py
# Handles store objects for each player

import stats

class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)
        self.dailySales = 0
        self.totalSales = 0
        self.totalrevenue = 0
        self.dailyrevenue = 0
        self.opDays = 0
        self.rating = 0
        self.totalRating = 0
        self.numRatings = 0

        self.menu = []
        self.inventory = {}

        # self.stats = []
        # daily sales, daily revenue, daily profit

        self.salesData = []
        self.revenueData = []
        self.profitData = []

# need inventory attributes

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def changePrice(self, price):
        self.price = int(price)

    def processSale(self):
        self.dailySales += 1
        self.dailyrevenue += self.price

    def getDailyRevenue(self):
        return self.dailyrevenue

    def aggregateRevenue(self):
        self.totalrevenue += self.dailyrevenue
        self.revenueData.append(self.dailyrevenue)
        self.dailyrevenue = 0
        self.totalSales += self.dailySales
        self.salesData.append(self.dailySales)
        self.dailySales = 0
        self.opDays += 1

    def getTotalRevenue(self):
        return self.totalrevenue

    def getOpDays(self):
        return self.opDays

    def getDailySales(self):
        return self.dailySales

    def getTotalSales(self):
        return self.totalSales

    def showStats(self):
        stats.generateGraph(self.salesData, "Daily Sales", self.revenueData, "Daily Revenue")
#        stats.generateGraph(self.revenueData, "Daily Revenue")

    def getRating(self):
        return self.rating

    def addRating(self, rating):
        self.totalRating += rating
        self.numRatings += 1
        self.rating = self.totalRating / self.numRatings

# def addMenuItem(self):
# def addInventoryItem(self):
# def purchaseItem(self):
