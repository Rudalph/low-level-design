from abc import ABC, abstractmethod

class Client:
    def __init__(self, report):
        self.report = report
    
    def get_report(self):
        value = self.report.get_json_data()
        print(value)
        
class Report(ABC):
    @abstractmethod
    def get_json_data(self):
        pass

class XMLDataProviderAdapter(Report):
    def __init__(self, provider):
        self.XMLDataProvider = provider
        
    def get_json_data(self):
        xml_data = self.XMLDataProvider.get_xml_data()
        json_data = xml_data + ' + JSON Data'
        return json_data

class XMLDataProvider:
    def get_xml_data(self):
        return 'XML Data'
    
provider = XMLDataProvider()
adapter = XMLDataProviderAdapter(provider)
client = Client(adapter)
client.get_report()
    
