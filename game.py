# game.py
# Runs the entire game/simulation

import population
import store

p = population.generatePopulation(5)
print(p)

myStoreName = input("Please select your store's name: ")
myStorePrice = input("Please select what price to sell your boba: ")
print("----------------------\n")
myStore = store.Store(myStoreName, myStorePrice)
#print(myStore)

# At the moment preferences only contains maximum value point (how much the customer is willing to pay at most)
sales = None
days = 0
while (myStore.getPrice() < 11 and sales != 0):
    sales = 0
    for i in p:
        if (i > myStore.getPrice()):
            myStore.processSale()
            sales += 1

    print("There are " + str(len(p)) + " potential customers.")
    print("We had " + str(sales) + " sales at $" + str(myStore.getPrice()) + " per sale.")
    print("We made $" + str(myStore.getDailyRevenue()) + " today.")
    print("----------------------\n")
    myStore.changePrice(myStore.getPrice() + 1)
    myStore.aggregateRevenue()
    days += 1

print("In total, we operated for " + str(days) + " days and made $" + str(myStore.getTotalRevenue()) + " in revenue.")
