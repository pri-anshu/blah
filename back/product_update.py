from data_unpacking import *
from read_data import read_data


class product_update:
    def update_data(item, quan, price):
        print(item)
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
        read_data.editdata(temp, r"back\data")
