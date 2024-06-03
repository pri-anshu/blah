import getpass
from read_data import read_data
from new_user import new_user
from store_updating import store_updating


class authen:
    unp = (
        r"C:\Users\PSINGH87\Music\python training (personal)\OOPS\store orcestation\unp"
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
                    authen.admin_usecase()
                    return
                else:
                    password = getpass.getpass("--> Enter your password again: ")
                    trial += 1
        else:
            print("-- Invalid username! --")
            exit(0)

    def admin_usecase():
        flag = input("System--> Do you wish to add new user or edit the store? ")
        if flag == "new user":
            new_user.new_user(authen.unp)
            # new_user.new_user(authen.database, authen.unp)
        elif flag == "edit store":
            store_updating.add_stock()
        else:
            print("invalid input")
        print("verified username for real ")
