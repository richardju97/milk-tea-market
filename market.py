# market.py
# Contains information about the entire market (e.g. supply costs)

import rawmaterials
import store

class Event:
    def __init__():
        self.action = 0

boba = rawmaterials.RawMaterial("Boba", 0, 0)
rent = rawmaterials.RawMaterial("Rent", 0, 0)
tea = rawmaterials.RawMaterial("Tea", 0, 0)

#print (boba.getName())
#print (boba.getPrice())

def createMarket(n):
    a = []
    for x in range(0, n):
    
        myStoreName = input("Please select your store's name: ")
        myStorePrice = input("Please select what price to sell your boba: ")
        print("----------------------\n")
        a.append(store.Store(myStoreName, myStorePrice))
    return a

#myStore = store.Store(myStoreName, myStorePrice)
#print(myStore)
