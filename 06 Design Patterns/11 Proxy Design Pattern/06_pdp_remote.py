from abc import ABC, abstractmethod

class Data(ABC):
    def get_data(self):
        pass
    
class DataService(Data):
    def get_data(self):
        return 'Data Provided by DataService Class'
    
class DataServiceProxy(Data):
    def __init__(self):
        print('Initilizing connection with remote DataService class')
        self.data_service = DataService()
        
    def get_data(self):
        res = self.data_service.get_data()
        return res
    
client = DataServiceProxy()
print(client.get_data())