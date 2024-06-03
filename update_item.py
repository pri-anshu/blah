from data import *
from product_update import product_update


class update_item:
    def add_items(item):
        value = int(input("Enter the quantity to be added- "))
        quan = data.stock.get(item) + value
        data.stock.update({item: quan})

        temp = input("do you wish to update the price? ")
        if temp == "yes":
            price = input("Enter the price of the item: ")
            data.shelf.update({item: price})
            product_update.update_data(item, value, price)
        else:
            print("adding item to stock without updating price")
