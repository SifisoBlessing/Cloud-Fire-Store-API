from main.DataBase import FireBase
from main.Domain.IDGenerators import CustomerID, ProductID


class Compensated:
    __customer_id = ""
    __name = ""
    __surname = ""
    __email = ""
    __product_id = ""
    __amount = 0

    def __init__(self,data):
        self.__data = data
        self.__setProductID()
        self.__setCustomerID()
        self.__db = FireBase.FireBase(self.__data, "compensated")

    def getData(self):
        pass

    def postData(self):
        return self.__db.postData()

    def __setProductID(self):
        product = str(self.__data["product_name"]).split(" ")
        initials = ""
        for i in product:
            initials += i[0]
        productID = ProductID.ProductID(initials)
        self.__data["product_id"] = productID.getID()

    def __setCustomerID(self):
        name = self.__data["name"]
        surname = self.__data["surname"]
        numID = 0
        customerID = CustomerID.CustomerID(name, surname, numID)
        self.__data["cutomer_id"] = customerID.getID()
