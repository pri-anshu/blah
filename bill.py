from tabulate import tabulate


class bill:
    slip = {}

    def add_to_bill(name, quan, price):
        bill.slip[name] = quan, price
        print(bill.slip)

    def display_bill():
        print(bill.slip)

        

        head = ["Item", "Quantity", "Rate"]
        table = []
        for key, values in bill.slip.items():
            table.append([key] + list(values))

        sum = 0
        for i in bill.slip:
            sum = sum + bill.slip[i][1]
        table.append(["TOTAL PRICE"] + [""] + [sum])
        print(tabulate(table, headers=head, tablefmt="grid"))

        exit(0)
