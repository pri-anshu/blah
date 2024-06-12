from read_data import read_data


class data:
    product_price = {}
    product_quan = {}
    temp = read_data.readdata((r"back\data"))
    key_list = [i for i in temp]
    value_list = []
    for i in range(len(temp)):
        value_list.append(list(temp[key_list[i]].strip().split(",")))
    # value_list=[temp.values]
    # for i in range(len(temp)):
    #     if key_list[i] in temp:
    #         print(temp.values)
    for i in range(len(value_list)):
        product_price.update({key_list[i]: value_list[i][0]})
        product_quan.update({key_list[i]: value_list[i][1]})

    def quotes_remover(dicts):
        for s in dicts:
            for keys in dicts:
                dicts[keys] = int(dicts[keys])

    quotes_remover(product_price)
    quotes_remover(product_quan)
