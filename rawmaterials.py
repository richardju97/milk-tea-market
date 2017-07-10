# rawmaterials.py
# All data pertaining to raw materials that each cafe can purchase

class RawMaterial:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def adjustPrice(self, delta):
        self.price += delta

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price
