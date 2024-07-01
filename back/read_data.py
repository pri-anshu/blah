class read_data:
    def readdata(n):
        file = n
        with open(file, "r") as file:
            lines = file.readlines()
            res = {}
            for line in lines:
                key, value = line.strip().split(":")
                res[key.strip()] = value.strip()
            return res

    def editdata(data, n):
        file = n
        res = data
        with open(file, "a") as file:
            for key, value in res.items():
                file.write(f"{key}: {value}\n")
        print("System--> Data updated successfully.")

    def remove_line(item,file):
        try:
            with open(file, 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open(file, 'w') as fw:
                    for line in lines:
                        if line != item:
                            fw.write(line)
                        ptr += 1
            print("Deleted")
            
        except:
            print("Oops! something error")


    def erasedata(n):
        file=n
        with open(file,"r+") as file:
            file.truncate()
