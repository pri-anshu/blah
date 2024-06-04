from order import take_order
from authen import authen


class index:
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
