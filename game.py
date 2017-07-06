# game.py
# Runs the entire game/simulation

import population
import store

p = population.generatePopulation(5)
print(p)

myStoreName = input("Please select your store's name: ")
myStorePrice = input("Please select what price to sell your boba: ")
myStore = store.Store(myStoreName, myStorePrice)
#print(myStore)

for i in p:
    if (True):
        myStore.processSale()

print("There are " + str(len(p)) + " customers")
print("We had " + str(len(p)) + " sales at $" + str(myStore.getPrice()))
print("We made $" + str(myStore.getDailyRevenue()) + " today.")
