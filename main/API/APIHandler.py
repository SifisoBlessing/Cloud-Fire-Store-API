from main.Domain.Customers.DepositedUsers import Deposited
from main.Domain.Customers.CompensatedUsers import Compensated
from main.Domain.Customers.UnsettledUsers import Unsettled


class APIHandler:
    def deposited(self, data):
        deposited = Deposited.Deposited(data)
        print(deposited.postData())

    def unsettled(self, data):
        unsettled = Unsettled.Unsettled(data)
        print(unsettled.postData())

    def compensated(self, data):
        com = Compensated.Compensated(data)
        print(com.postData())
