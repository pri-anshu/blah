from data import *
from home import product
from bill import bill
from delete import delete


class take_order:
    def ordering():
        print(data.key_list)
        loop = True
        while loop == True:
            run = True
            while run == True:
                a = input("--> Enter the item that is to be ordered- ")
                if a not in data.shelf:
                    print("Item not found in the store, try different item.")
                else:
                    print(
                        "Item found, Priced at- ",
                        data.shelf.get(a),
                        ", quantity available- ",
                        data.stock.get(a),
                    )
                    run = False
            b = int(input("Enter the required quantity- "))
            if b > data.stock.get(a):
                print("Sorry requied quantity isn't available")
                print("quantity available- ", data.stock.get(a))
            else:
                item = product(a, data.shelf.get(a), b)
                item()
                choice = input("Do you wish to continue? ")
                if choice == "yes":
                    loop = True
                elif choice == "no":
                    loop = False
                    order = input("Would you like to delete any item from order? ")
                    if order == "yes":
                        delete.remove_item()
                    else:
                        pass
                    bill.display_bill()
