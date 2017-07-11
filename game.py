# game.py
# Runs the entire game/simulation

from random import randint
import population
import store
import market

print("Welcome to Milk Tea Mania! Please configure your settings:")
numPlayers = int(input("Enter Number of Players Playing: "))
populationSize = int(input("Enter desired population size for this simulation: "))
maxDays = int(input("Enter maximum number of operation days: "))
#allPlayers = []

print("----------------------\n")

#for x in range(0, numPlayers):
#
#    myStoreName = input("Please select your store's name: ")
#    myStorePrice = input("Please select what price to sell your boba: ")
#    print("----------------------\n")
#    allPlayers.append(store.Store(myStoreName, myStorePrice))
#    #myStore = store.Store(myStoreName, myStorePrice)
#    #print(myStore)

allPlayers = market.createMarket(numPlayers)

p = population.generatePopulation(populationSize)
print(p) #only here for dev/debugging purposes
print("There are " + str(len(p)) + " potential customers.")
print("----------------------\n")

# At the moment preferences only contains maximum value point (how much the customer is willing to pay at most)
#sales = None
#days = 0
day = 0
while (day != maxDays):
#while (allPlayers[0].getPrice() < 11 and sales != 0):
#    sales = 0
    for i in p:
        if (i >= allPlayers[0].getPrice()):
            # for now we assume that all places have the same price
            decision = randint(0, numPlayers-1)
            allPlayers[decision].processSale()
#            sales += 1

    print("Day " + str(day+1))
    for x in range(0, numPlayers):
        print(str(allPlayers[x].getName()) + " had " + str(allPlayers[x].getDailySales()) + " sales at $" + str(allPlayers[x].getPrice()) + " per sale, earning a total of " + str(allPlayers[x].getDailyRevenue()))
#        print("We made $" + str(allPlayers[x].getDailyRevenue()) + " today.")
#        print("----------------------\n")
        allPlayers[x].changePrice(allPlayers[x].getPrice() + 1)
        if (allPlayers[x].getDailyRevenue() != 0):
            allPlayers[x].aggregateRevenue()
#        days += 1
    day += 1
    print("----------------------\n")

print("End of Simulation Results:")

for y in range(0, numPlayers):
    print(str(allPlayers[y].getName()) + " operated for " + str(allPlayers[y].getOpDays()) + " days and made $" + str(allPlayers[y].getTotalRevenue()) + " in revenue.")
    allPlayers[y].showStats()
