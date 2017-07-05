# population.py
# Contains the entire population (customers) of your market

import customer

marketSize = 5

#A = customer.Customer()
#print(A.getPreferences())

population = []

for i in range(0, marketSize):
    population.append(customer.Customer().getPreferences())

print(population)
