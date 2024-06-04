from data import *
from home import product
from bill import bill
from delete import delete


class take_order:
    def ordering():
        loop = True
        while loop == True:
            run = True
            while run == True:
                for products in range(len(data.key_list) - 1):
                    print(data.key_list[products].upper(), end=", ")
                print(data.key_list[-1].upper(), "\n")
                print("Enter the item to be ordered-")
                a = input("- ")
                if a not in data.shelf:
                    print("Item not found in the store,",
                          "try different item.")
                else:
                    print(
                        "Item found, Priced at- ",
                        data.shelf.get(a),
                        ", quantity available- ",
                        data.stock.get(a),
                    )
                    run = False
            print("Enter the required quantity-")
            b = int(input("- "))
            if b > data.stock.get(a):
                print("Sorry requied quantity isn't available",
                      "quantity available- ", data.stock.get(a))
            elif b==0:
                print("Sorry can't order quantity 0")
            else:
                item = product(a, data.shelf.get(a), b)
                item()
                choice = input("Do you wish to continue? ")
                if choice.lower() == 'yes':
                    loop = True
                elif choice.lower() == 'no':
                    loop = False

                    print("Would you like to delete any item from order?")
                    order = input("- ")
                    if order.lower() == 'yes':
                        delete.remove_item()
                    # else:
                    #     pass
                    bill.display_bill()
