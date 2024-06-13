from read_data import read_data
# from index import index


class new_user:
    # def new_user(n):
    #     a = {}
    #     print("System--> Adding new store admin")
    #     new_username = input("System--> Enter the new username: ")
    #     new_password = input("System--> Password for new user: ")
    #     a[new_username] = new_password
    #     read_data.editdata(a, n)

    def new_user(n, z,database):
        a={}
        new_username = input("{}--> ".format(z))
        if new_username in database:
            print("\nSystem--> User Already exist in Database")
            print('System--> Please enter a new user')
            a=new_user.new_user(n,z,database)
            return a

        elif new_username=='exit':
            a=False
            return a

        else:
            print("System--> Password for new user:")
            new_password = input("{}--> ".format(z))
            a[new_username] = new_password
            read_data.editdata(a, n)
            return a

        # new_user.making_user(n,database,z)

    # def making_user(n,database,z):
    #     a={}
    #     temp=True
    #     while temp==True:
    #         new_username = input("{}--> ".format(z))
    #         if new_username in database:
    #             print("\nSystem--> User Already exist in Database")
    #             print('System--> Please enter a new user')
    #             new_user.making_user(n,database,z)
    #         elif new_username=='exit':
    #             print('exit function')
    #             temp=False
    #         else:
    #             # break
    #             print("System--> Password for new user:")
    #             new_password = input("{}--> ".format(z))
    #             a[new_username] = new_password
    #             read_data.editdata(a, n)
    #             return a

        # elif new_username is 'exit':

            # sys.exit(0)
            # exit()
            # index.start()
            #pass #circular interitance while using start() from index

        # else:
        #     break