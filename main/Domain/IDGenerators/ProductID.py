class ProductID:

    def __init__(self, pi):
        self.pi = pi

    def __product_id(self):
        id = ""
        product = self.pi.upper()
        for string in product:
            id = id + f"{(ord(string))}"
        return id

    def __product_id_cloud(self, id):
        storage = "/home/sci-fi/Documents/sandiy/fili/assets/product_id_storage.txt"
        with open(storage, "a") as file:
            file.write(id)
            file.write("\n")

    def getID(self):
        protuctID = self.__product_id()
        self.__product_id_cloud(protuctID)
        return protuctID
