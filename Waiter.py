#Kevin Shu, kyshu@usc.edu
#ITP 115, Spring 2021
#MenuItem Class

import Menu
import Diner

class Waiter(object):

    def __init__(self, menu):
        self.menu = menu
        self.diners = []

    def addDiner(self, diner):
        self.diners.append(diner)

    def getNumDiners(self):
        return len(self.diners)

    #just making a loop to print out the statuses and who belongs in them
    def printDinerStatuses(self):
        STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
        for status in STATUSES:
            print("Diners who are " + status + ":")
            for diner in self.diners:
                if STATUSES[diner.status] == status:
                    print(diner)


    def takeOrders(self):
        CATEGORIES = ["Drink", "Appetizer", "Entree", "Dessert"]
        #loop through every diner the waiter is serving
        for diner in self.diners:
            #if they are ordering then print the menu
            if diner.getStatus() == 1:
                #loop through every menu category
                for category in CATEGORIES:
                    #print every item in that category
                    self.menu.printMenuItems(category)
                    #take the order
                    order = int(input("> "))
                    #if the order isn't valid, keep going until it is
                    while order not in range(0, self.menu.getNumMenuItems(category)):
                        order = int(input("> "))
                    #add the valid order to the diner's list of menuItems
                    diner.addToOrder(self.menu.getMenuItem(category, order))
                #print out the order outside of the loop going thru the categories
                diner.printOrder()

    def printMealCost(self):
        for diner in self.diners:
            #check to see if the status of the diner is paying
            if diner.getStatus() == 3:
                total = "{:.2f}".format(diner.getMealCost())
                print("\t" + diner.getName() + ", your meal cost is $" + total)

    def removeDiners(self):
        #make the range inclusive of 0
        for i in range(len(self.diners)-1, -1, -1):
            if self.diners[i].getStatus() == 4:
                print(self.diners[i].getName() + ", thank you for dining with us! Come again soon!")
                del self.diners[i]

    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.printMealCost()
        self.removeDiners()
        for diner in self.diners:
            diner.updateStatus()












