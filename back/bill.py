from tabulate import tabulate
from stock_reduction import stock_reduction

class bill:
    slip = {}
    head = ["Item", "Quantity", "Rate"]

    def add_to_bill(name, quan, price):
        bill.slip[name.upper()] = quan, price
        # head=["Item","Quantity","Rate"]
        bill_table = []
        for key, values in bill.slip.items():
            bill_table.append([key] + list(values))
        print(tabulate(bill_table, headers=bill.head, tablefmt="grid"))



    def display_bill():
        print(bill.slip)

        bill_table = []
        for key, values in bill.slip.items():
            bill_table.append([key] + list(values))
        stock_reduction.stock_reduction(bill.slip)
        sum = 0
        for i in bill.slip:
            sum = sum + bill.slip[i][1]

        bill_table.append(["TOTAL PRICE"] + [""] + [sum])
        print(tabulate(bill_table, headers=bill.head, tablefmt="grid"))

        exit(0)
