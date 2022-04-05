import datetime
from dateutil.relativedelta import relativedelta
from main.DataBase import FireBase
from main.Domain.IDGenerators import CustomerID, ProductID


class Unsettled:

    def __init__(self, data):
        self.__data = data
        self.__setProductID()
        self.__setCustomerID()
        self.__setTimeStamp()
        self.__db = FireBase.FireBase(self.__data, "unsettled")

    def __setTimeStamp(self):
        today = datetime.date.today()
        three_mon_rel = relativedelta(months=4)
        self.__data["value"] = f"{today + three_mon_rel}"

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
        self.__data["customer_id"] = customerID.getID()