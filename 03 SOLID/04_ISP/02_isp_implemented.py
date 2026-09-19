from abc import ABC, abstractmethod

# Interface 1
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

# Interface 2
class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Interface 2
class Fax(ABC):
    @abstractmethod
    def fax_document(self):
        pass


# Multifunction Printer Class that needs all the functionalities 
class MultifuctionPrinter(Printer, Scanner, Fax):
    def print_document(self):
        print("Multifunction Printer printing document")
    
    def scan_document(self):
        print("Multifunction Printer scanning document")
    
    def fax_document(self):
        print("Multifunction printer fax document")


# Simpler Printer class that needs only printer functionality    
class SimplePrinter(Printer):
    def print_document(self):
        print("Simple Printer printing document")
        

mfp = MultifuctionPrinter()
mfp.print_document()
mfp.fax_document()
mfp.scan_document()

sp = SimplePrinter()
sp.print_document()