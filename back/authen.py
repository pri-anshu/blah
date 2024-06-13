import getpass
from read_data import read_data
from new_user import new_user
from store_updating import store_updating


class authen:
    unp = (
        r"back\unp"
    )
    database = read_data.readdata(unp)

    def authentication():
        trial = 0

        username = input("--> Enter your Username: ")
        password = getpass.getpass("--> Enter your password: ")

        if username in authen.database.keys():
            while trial < 2:
                if password == authen.database.get(username):
                    print("   ACCESS GRANTED")
                    authen.admin_usecase(username)
                    return
                else:
                    print("--> Enter your password again: ")
                    password = getpass.getpass("--> Enter your password again: ")
                    trial += 1
        else:
            print("-- Invalid username! --")
            exit(0)

    def admin_usecase(z):
        print("System--> Do you wish to add new user or edit the store?")
        flag = input("{}--> ".format(z))

        if flag.lower() == "new user":

            # authen.database.update(new_user.new_user(authen.unp, z,authen.database))
            # new_user.new_user(authen.database, authen.unp)

            print("System--> Adding new store admin")
            print("System--> Enter the new username:")

            while True:
                a=new_user.new_user(authen.unp,z,authen.database)
                if a == False:
                    print("-- Exiting Process --")
                    break
                if a is not False:
                    authen.database.update(a)
                    print("-- User Created --")
                    break

        elif flag.lower() == "edit store":
            store_updating.add_stock(z)

        else:
            print("-- invalid input--")
        print("-- verified --")




    # def admin_usecase(z):
    #     print("System--> Select one from below options\n  -> 1. new user\n  -> 2. edit store"
    #     )
    #     flag = input("{}--> ".format(z))
    #     if flag == "new user":
    #         authen.database.update(new_user.new_user(z))
    #     elif flag == "edit store":
    #         store_updating.add_stock(z)
    #     else:
    #         print("System--> Invalid input")
    #     print("System--> Verified")
