# game.py
# Runs the entire game/simulation

import population
import store

numPlayers = int(input("Enter Number of Players Playing: "))
populationSize = input("Enter desired population size for this simulation: ")
allPlayers = []

for x in range(0, numPlayers):

    myStoreName = input("Please select your store's name: ")
    myStorePrice = input("Please select what price to sell your boba: ")
    print("----------------------\n")
    allPlayers.append(store.Store(myStoreName, myStorePrice))
    #myStore = store.Store(myStoreName, myStorePrice)
    #print(myStore)

p = population.generatePopulation(int(populationSize))
print(p)

# At the moment preferences only contains maximum value point (how much the customer is willing to pay at most)
sales = None
days = 0
while (allPlayers[0].getPrice() < 11 and sales != 0):
    sales = 0
    for i in p:
        if (i >= allPlayers[0].getPrice()):
            allPlayers[0].processSale()
            sales += 1

    print("There are " + str(len(p)) + " potential customers.")
    print("We had " + str(sales) + " sales at $" + str(allPlayers[0].getPrice()) + " per sale.")
    print("We made $" + str(allPlayers[0].getDailyRevenue()) + " today.")
    print("----------------------\n")
    allPlayers[0].changePrice(allPlayers[0].getPrice() + 1)
    allPlayers[0].aggregateRevenue()
    days += 1

print("In total, we operated for " + str(days) + " days and made $" + str(allPlayers[0].getTotalRevenue()) + " in revenue.")
