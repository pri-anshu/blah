from read_data import read_data


class new_user:
    def new_user(n):
        a = {}
        print("adding new store admin")
        new_username = input("Enter the new username: ")
        new_password = input("Password for new user: ")
        a[new_username] = new_password
        read_data.editdata(a, n)
