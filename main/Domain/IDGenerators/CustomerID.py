class CustomerID:

    def __init__(self, name, surname, number_ID):
        self.name = name
        self.surnmae = surname
        self.numberID = number_ID

    def __customer_number(self, number_id):
        number = 0
        for i in range(1, number_id + 1):
            number = f"#{'0' * (2 - len(str(i))) + str(i)}"

        return number

    def __customer(self, fname, lname, number):
        id = fname[0] + fname[-1] + lname[0] + lname[-1]
        customer_id = f"{number}{''.join(id)}"
        return customer_id

    def customer_id_cloud(self, fname, lname, customer_id, ):
        storage = "/home/sci-fi/Documents/sandiy/fili/assets/customer_id_storage.txt"
        with open(storage, "a") as file:
            file.write(f"{fname.lower().capitalize()} {lname.lower().capitalize()} : {customer_id}")
            file.write("\n")

    def getID(self):
        fname = self.name.upper()
        lname = self.surnmae.upper()
        number_id = int(self.numberID)

        number = self.__customer_number(number_id)
        customer_id = self.__customer(fname, lname, number)
        self.customer_id_cloud(fname, lname, customer_id)

        return customer_id
