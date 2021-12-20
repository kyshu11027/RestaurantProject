# Run.py
# ITP 115, Spring 2021 Final project
# Run this file in order to start the restaurant simulation program

import datetime
import time

# TODO 1: uncomment the following 3 import statements once you created these files/classes
from Menu import Menu
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper


def main():
    # TODO 2: in the following line, add your own restaurant name in the quotes
    RESTAURANT_NAME = "Python Place"
    restaurantTime = datetime.datetime(2021, 5, 1, 5, 0)

    # Create the Menu object
    # TODO 3: uncomment the following line once the Menu class is implemented
    menu = Menu("menu.csv")

    # create the waiter object using the Menu object we just created
    # TODO 4: uncomment the following line once the Waiter class is implemented
    waiter = Waiter(menu)
    print("Welcome to " + RESTAURANT_NAME + "!")
    print(RESTAURANT_NAME + " is now open for dinner.\n")

    for i in range(21):
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=15)

        # TODO 3: uncomment the following 3 lines once the Diner class is implemented
        potentialDiner = RestaurantHelper.randomDinerGenerator()
        if potentialDiner is not None:
             print("\n" + potentialDiner.getName() + " welcome, please be seated!")
            # we have a diner to add to the waiter's list of diners

            # TODO 4: uncomment the following line once the Waiter class is implemented
             waiter.addDiner(potentialDiner)   # Make sure to keep this line inside the if-statement on line 34!

        # TODO 5: uncomment the following line once the Waiter class is implemented
        waiter.advanceDiners()  # Keep this line outside of the if-statement
        time.sleep(2)

    print("\n~~~ ", RESTAURANT_NAME, "is now closed. ~~~")
    # After the restaurant is closed, progress any diners until everyone has left
    # TODO 6: uncomment the following 5 lines once the Waiter class is implemented
    while waiter.getNumDiners():
         print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
         restaurantTime += datetime.timedelta(minutes=15)
         waiter.advanceDiners()
         time.sleep(2)

    print("Goodbye!")


main()
