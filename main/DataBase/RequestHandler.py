class RequestHanlder:

    def __init__(self, data):
        self.__data = data
        self.__setValues()
        self.__convert()

    def __setValues(self):
        self.__name = self.__data["name"]
        self.__surname = self.__data["surname"]
        self.__customerID = self.__data["customer_id"]
        self.__email = self.__data["email"]
        self.__productName = self.__data["product_name"]
        self.__productID = self.__data["product_id"]
        self.__category = self.__data["category"]
        self.__val = self.__data["value"]

    def __convert(self):
        self.__object = {
            "name": self.__name,
            "surname": self.__surname,
            "customerID": self.__customerID,
            "product": {
                "category": self.__category,
                "item": self.__productName,
                "id": self.__productName
            },
            "amount": self.__val
        }

    def getData(self):
        return self.__data

    def getID(self):
        return self.__customerID
