from read_data import read_data


class data:
    shelf = {}
    stock = {}
    temp = read_data.readdata((r"data.txt"))
    key_list = [i for i in temp]

    value_list = []

    for i in range(len(temp)):
        value_list.append(list(temp[key_list[i]].strip().split(",")))

    # value_list=[temp.values]
    # for i in range(len(temp)):
    #     if key_list[i] in temp:
    #         print(temp.values)

    for i in range(len(value_list)):
        shelf.update({key_list[i]: value_list[i][0]})
        stock.update({key_list[i]: value_list[i][1]})

    def quotes_remover(dicts):
        for s in dicts:
            for keys in dicts:
                dicts[keys] = int(dicts[keys])

    quotes_remover(shelf)
    quotes_remover(stock)
