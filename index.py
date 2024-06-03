from order import take_order
from authen import authen


class index:
    def start():
        flag = True
        while flag == True:
            choice = input("User or Admin or Exit? ")
            if choice == "user":
                take_order.ordering()
            elif choice == "admin":
                authen.authentication()
            elif choice == "exit":
                print("exiting store, thank you for visit!")
                flag = False
            else:
                print("invalid input")

    start()
