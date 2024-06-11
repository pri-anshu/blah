from data import *
from product_update import product_update


class update_item:
    def add_items(item, z):
        print("Enter the quantity to be added-")
        value = int(input("{}--> ".format(z)))
        quan = data.product_quan.get(item) + value
        data.product_quan.update({item: quan})
        print("System--> Do you wish to update the price?")
        temp = input("{}--> ".format(z))
        if temp.lower() == "yes":
            print("System--> Enter the price of the item:")
            price = input("{}--> ".format(z))
            data.product_price.update({item: price})
            product_update.update_data(item, value, price)
        else:
            print("Adding item to stock without updating price")
