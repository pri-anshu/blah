from bill import bill


class delete:
    def remove_item():
        item = input("Please enter the item you would like to delete- ")
        if item in bill.slip:
            print("Removing ", item, " from the bill.")
            bill.slip.pop(item)
            print(bill.slip)
        else:
            print("item not found in bill")
