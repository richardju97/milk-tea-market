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

print("----------------------\n")

allPlayers, allRawMaterials = market.createMarket(numPlayers)

p = population.generatePopulation(populationSize)
print(p) #only here for dev/debugging purposes
print("There are " + str(len(p)) + " potential customers.")
print("----------------------\n")

# At the moment preferences only contains maximum value point (how much the customer is willing to pay at most)
day = 0
while (day != maxDays):
#while (allPlayers[0].getPrice() < 11 and sales != 0):
    for i in p:
        if (i >= allPlayers[0].getPrice()):
            # for now we assume that all places have the same price
            decision = randint(0, numPlayers-1)
            allPlayers[decision].processSale()
            allPlayers[decision].addRating(randint(1, 5))

    print("Day " + str(day+1))
    for x in range(0, numPlayers):
        print(str(allPlayers[x].getName()) + " - Sales ($" + str(allPlayers[x].getPrice()) + "):x $" + str(allPlayers[x].getDailySales())  + " - Revenue: $" + str(allPlayers[x].getDailyRevenue()) + " - Rating: " + str(allPlayers[x].getRating()))
        allPlayers[x].changePrice(allPlayers[x].getPrice() + 1)
        if (allPlayers[x].getDailyRevenue() != 0):
            allPlayers[x].aggregateRevenue()
    day += 1
    print("----------------------\n")

allPlayers[0].purchaseItem(allRawMaterials[0])

print("End of Simulation Results:")

for y in range(0, numPlayers):
    print(str(allPlayers[y].getName()) + " - Operation Days: " + str(allPlayers[y].getOpDays()) + " - Revenue: $" + str(allPlayers[y].getTotalRevenue()) + " - Rating: " + str(allPlayers[y].getRating()))
    allPlayers[y].showStats()
    print(allPlayers[0].getInventory())
