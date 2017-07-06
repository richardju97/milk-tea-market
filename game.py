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

# At the moment preferences only contains maximum value point (how much the customer is willing to pay at most)
sales = 0
for i in p:
    if (i > myStore.getPrice()):
        myStore.processSale()
        sales += 1

print("There are " + str(len(p)) + " possible customers")
print("We had " + str(sales) + " sales at $" + str(myStore.getPrice()))
print("We made $" + str(myStore.getDailyRevenue()) + " today.")
