from data import *
from bill import bill


class product:
    def __init__(self, name, price, quan):
        self.name = name
        self.price = price
        self.quan = quan
        print("instance created")

    def __call__(self):
        total = self.quan * self.price
        bill.add_to_bill(self.name, self.quan, total)
