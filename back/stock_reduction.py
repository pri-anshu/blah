from data_unpacking import data
from read_data import read_data
from product_update import product_update

class stock_reduction():
    # def unpacking(database):    

    def stock_reduction(bill_data):
        print(bill_data)
        kl = [i for i in bill_data]
        print(kl)

        vl=[]
        prod_price={}
        prod_quan={}

        file=r"back\data"
        database=read_data.readdata(file)

        key_list=[i for i in database]

        # stock_reduction.unpacking(database)

        for i in range(len(database)):
            vl.append(list(database[key_list[i]].strip().split(",")))
        for i in range(len(vl)):
            prod_price.update({key_list[i]: vl[i][0]})
            prod_quan.update({key_list[i]: vl[i][1]})
        prod_quan=data.quotes_remover(prod_quan)
        prod_price=data.quotes_remover(prod_price)

        print(prod_price)
        print(prod_quan)

        # print(prod_quan['potato'])
        # print(bill_data['POTATO'][0])


        for key in kl:
            # read_data.remove_line(key,file)

            if key.casefold() in prod_quan:
                temp=(prod_quan[key.casefold()])-(bill_data[key][0])
                print(temp)
                # prod_quan.update[key]=temp
        # print(prod_quan)
                rmline=key.lower()+": "+str(prod_price[key.casefold()])+","+str(prod_quan[key.casefold()])+"\n"
                print(rmline)

                dline={key.lower():bill_data[key]}
                read_data.editdata(dline,r"back\saved_orders")

                read_data.remove_line(rmline,file)

                product_update.update_data(key.lower(),temp,prod_price[key.casefold()])


        # [i.lower() for i in key_list]

        # for i in key_list:
        #     for j in database:
        #         if i.lower() == j.lower():
        #             database.pop(j)

        # read_data.erasedata(file)
        # read_data.editdata(database,file)



        # with open(file, 'r') as file: 
        #     database = file.readlines() 

        # print(database) 
        # # database[1] = "Here is my modified Line 2\n"

        # file.seek(0)
        # for item in key_list:
        #     if item in :


        # with open(file, 'w') as file: 
        # #     file.writelines(database) 

        # for i in key_list:
        #     with open(file,"r+") as f:
        #         new_f = f.readlines()
        #         f.seek(0)
        #         f.truncate()
        #         for line in new_f:
        #             if i not in line:
        #                 f.writelines(line)
                        # f.write(line)


        print("deleted")
