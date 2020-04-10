import pymongo
from pymongo.errors import AutoReconnect
from pymongo.errors import NetworkTimeout
from pymongo.errors import NotMasterError
from Helper.JsonHandler import JsonHandler
import time

'''DataBaseHandler connects to the mongoDB to fetch the replicas priority list'''

class DbHandler:

    def __init__(self):
        self._jsonHandler = JsonHandler()
        self._config = self._jsonHandler.LoadJson('Config.json')
        self._polling = True

    def GetStatusCollection(self):
        print("--->In Db Handler")

        for attempts in range(self._config['dbReconnection']):
            try:
                Client = pymongo.MongoClient(self._config['connectionString'])
                dataBase = Client[self._config['dataBase']]
                collection = dataBase[self._config['collectionName']]
                self._polling = False
                return self._polling, collection
            except (AutoReconnect,NetworkTimeout) as ex:
                print("--->In Db Handler ex1")
                print(str(ex))
                waitTime = 5.0*attempts
                self._polling = True
                time.sleep(waitTime)
            except Exception as ex:
                print("--->In Db Handler ex2")
                print(str(ex))
                self._polling = True
                break
        return self._polling, None