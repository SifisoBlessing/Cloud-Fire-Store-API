import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from main.DataBase import RequestHandler


class FireBase:
    def __init__(self, data, collection):
        self.__initialise()
        self.__requestHandler = RequestHandler.RequestHanlder(data)
        self.__collection = collection
        self.__db = firestore.client()

    def __initialise(self):
        cred = credentials.Certificate("/home/sci-fi/Documents/sandiy/creds/fb_service_account.json")
        firebase_admin.initialize_app(cred)

    def getData(self):
        collection = self.__db.collection(self.__collection)

    def postData(self):
        id = self.__requestHandler.getID()
        data = self.__requestHandler.getData()
        self.__db.collection(self.__collection).document(id).set(data)
        return data