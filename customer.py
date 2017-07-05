# customer.py
# Contains everything to do with the customer object

from random import randint

class Customer:
    def __init__(self):
        self.preferences = randint(0, 100)

    def getPreferences(self):
        return self.preferences

# Test
#A = Customer()
#print(A.getPreferences())
