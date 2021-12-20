#Kevin Shu, kyshu@usc.edu
#ITP 115, Spring 2021
#MenuItem Class


class MenuItem(object):

    #initialization method
    def __init__(self, name, category, price, description):
        self.name = name
        self.category = category
        self.price = float(price)
        self.desc = description

    #defining all of the get methods
    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.desc

    #make sure that the price is a float not a string
    def __str__(self):
        cost = float(self.price)
        price = "{:.2f}".format(cost)
        return self.name + " (" + self.category + "): $" + price + "\n\t"+self.desc


