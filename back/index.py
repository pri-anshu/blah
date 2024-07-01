from order import take_order
from authen import authen
# from data_unpacking import data

class index:
    # feature of adding admin access to past orders and calculations as a bill print
    def start():
        flag = True
        while flag == True:
            choice = input("User or Admin or Exit? ")
            if choice.lower() == "user":
                take_order.ordering()
            elif choice.lower() == "admin":
                authen.authentication()
            elif choice.lower() == "exit":
                print("exiting store, thank you for visit!")
                flag = False
            else:
                print("-- Invalid Input --")

    start()
