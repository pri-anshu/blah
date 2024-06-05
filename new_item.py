from data import *
from product_update import product_update


class new_item:
    def add_new_item(item,z):
        print("System--> Item not found in the store.")
        print("System--> Do you wish to add new item?")
        temp = input("{}--> ".format(z))
        if temp.lower() == "yes":
            print("System--> Enter the quantity to be added-")
            quan = int(input("{}--> ".format(z)))
            data.product_quan.update({item: quan})
            print("System--> Enter the price of item-")
            price = int(input("{}--> ".format(z)))
            data.product_price.update({item: price})
            product_update.update_data(item, quan, price)
        elif temp.lower() == "no":
            print("-- Exiting, Thank You! --")
            exit(0)
        else:
            print("-- Invalid Input --")
