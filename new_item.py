from data import *
from product_update import product_update


class new_item:
    def add_new_item(item):
        print("item not found in the store.")
        temp = input("Do you wish to add new item? ")
        if temp == "yes":
            quan = int(input("Enter the quantity to be added- "))
            data.stock.update({item: quan})
            price = int(input("Enter the price of item- "))
            data.shelf.update({item: price})
            product_update.update_data(item, quan, price)
        elif temp == "no":
            print("exiting, thank you")
            exit(0)
        else:
            print("invalid input")
