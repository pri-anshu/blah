from data import *
from read_data import read_data


class product_update:
    def update_data(item, quan, price):
        print(item)
        # value = int(input("Enter the quantity to be added- "))
        # data.stock.update({item: value})
        # price = int(input("Enter the price of item- "))
        # data.shelf.update({item: price})
        # print(data.stock)
        # print(data.shelf)
        # upload_dict=test.merge_dicts(item,value,price)
        # read_data.editdata(upload_dict,r'OOPS\store orcestation\data.txthon ')
        # print(upload_dict)

        temp = {}
        t = []
        print(item)
        print(quan)
        print(price)

        t.append(price)
        t.append(quan)
        print(t)
        my_string = ",".join(map(str, t))

        temp.update({item: my_string})
        print(temp)

        read_data.editdata(temp, r"OOPS\store orcestation\data.txt")

    # def merge_dicts(quan,price):
    #     temp={}
    #     t=[]
    #     print(quan)
    #     print(price)
    #     for i in quan:
    #         t.append([quan[i],price[i]])
    #         print(t)
    #     key_list=[i for i in quan]
    #     for i in range(len(key_list)):
    #         temp.update({key_list[i]:t[i]})
    #     return temp

    # def update_data(item):
    #     value = int(input("Enter the quantity to be added- "))
    #     print("adding item to store.")
    #     data.stock.update({item: value})
    #     price = int(input("Enter the price of item- "))
    #     data.shelf.update({item: price})
    #     print(data.stock)
    #     print(data.shelf)
    #     upload_dict=product_update.merge_dicts(data.stock,data.shelf)
    #     read_data.editdata(upload_dict,r'OOPS\store orcestation\data.txthon ')
