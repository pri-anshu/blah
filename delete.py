from bill import bill


class delete:
    def remove_item():
        print("Please enter the item you would like to delete-")
        item = input("- ")

        if item.upper() in bill.slip:
            
            bill.slip.pop(item.upper())
            print("Removing ", item, " from the bill.")
        else:
            print("item not found in bill")

        print("Do you Still want to delete anymore items?")
        temp=input("- ")
        if temp.lower() == 'yes':
            delete.remove_item()
        else:
            pass