# store.py
# Handles store objects for each player

class Store:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def changePrice(self, price):
        self.price = price
