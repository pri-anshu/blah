from data import *
from home import product
from bill import bill
from delete import delete


class take_order:
    def ordering():
        loop1 = True
        while loop1 == True:
            loop2 = True
            while loop2 == True:
                for products in range(len(data.key_list) - 1):
                    print(data.key_list[products].upper(), end=", ")
                print(data.key_list[-1].upper(), "\n")
                print("Enter the item to be ordered-")
                I = input("- ")
                if I not in data.product_price:
                    print("Item not found in the store,", "try different item.")
                else:
                    print(
                        "Item found, Priced at- ",
                        data.product_price.get(I),
                        ", quantity available- ",
                        data.product_quan.get(I),
                    )
                    loop2 = False
            print("Enter the required quantity-")
            Q = int(input("- "))
            if Q > data.product_quan.get(I):
                print(
                    "Sorry requied quantity isn't available",
                    "quantity available- ",
                    data.product_quan.get(I),
                )
            elif Q == 0:
                print("Sorry can't order quantity 0")
            else:
                item = product(I, data.product_price.get(I), Q)
                item()
                print("Do you wish to continue?")
                choice = input("- ")
                if choice.lower() == "yes":
                    loop1 = True
                elif choice.lower() == "no":
                    loop1 = False

                    print("Would you like to delete any item from order?")
                    order = input("- ")
                    if order.lower() == "yes":
                        delete.remove_item()
                    # else:
                    #     pass
                    bill.display_bill()
