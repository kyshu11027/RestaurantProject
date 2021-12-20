#Kevin Shu, kyshu@usc.edu
#ITP 115, Spring 2021
#Menu Class

import MenuItem

class Menu(object):
    CATEGORIES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, fileName):
        fin = open(fileName, "r")
        header_line = fin.readline()
        #making the menu a dictionary with the keys the categories
        self.items = {"Drink": [], "Appetizer": [], "Entree": [], "Dessert": []}

        for line in fin:
            #reading each line and stripping the spaces and making them into lists split by the commas
            line.strip()
            tempList = line.split(",")
            #making a new menuItem for each line and appending them to the category's list
            newMenuItem = MenuItem.MenuItem(tempList[0], tempList[1], tempList[2], tempList[3])
            self.items[newMenuItem.category].append(newMenuItem)
        fin.close()

    def getMenuItem(self, category, index):
        if category in Menu.CATEGORIES:
            #make sure that the category and index are valid
            if 0 <= index < len(self.items[category]):
                return self.items[category][index]

    def printMenuItems(self, category):
        #error check to make sure the category is in the menu
        if category in Menu.CATEGORIES:
            number = 0
            print("-----" + category.upper() + "------")
            #print each item in the category
            for item in self.items[category]:
                print(str(number) + ") ", end="")
                print(item)
                number += 1

    def getNumMenuItems(self, category):
        if category in Menu.CATEGORIES:
            return len(self.items[category])
        else:
            return 0









