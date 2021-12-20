#Kevin Shu, kyshu@usc.edu
#ITP 115, Spring 2021
#Menu Class

import MenuItem

class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    #initializing the Diner object
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    #all of the get functions are pretty self explanatory
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.status

    #just adding to the local variable of the object
    def updateStatus(self):
        self.status += 1

    #adding to the diner's order list
    def addToOrder(self, item):
        self.order.append(item)

    #using loops to get thru all of the orders and formatting them
    def printOrder(self):
        print(self.name + " ordered:")
        for item in self.order:
            print("- ", end="")
            print(item)

    #just adding everything. Make sure the price is a float not a string!
    def getMealCost(self):
        total = 0
        for item in self.order:
            total += float(item.price)
        return total

    def __str__(self):
        return "\tDiner " + self.name + " is currently " + Diner.STATUSES[self.status] + "."