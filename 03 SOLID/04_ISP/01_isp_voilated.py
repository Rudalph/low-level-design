# Parent class
class Machine:
    def print_document(self):
        print("Printing Document")
    
    def scan_document(self):
        print("Scanning Document")
    
    def fax_document(self):
        print("Fax Document")
        
# Child class 1: Multi Functioin Printer
class MultiFunctionPrinter(Machine):
    def color_print(self, color):
        print(f"Printing Coloured Document: {color}")
# MultiFunction Printer is advanced printer and needs all parent function

# But now we have another child class
# Child class 2: Simple Printer
class SimplePrinter(Machine):
    def print_document(self):
        return super().print_document()
    
    def scan_document(self):
        print("Scanning not supported in simple printer")
        
    def fax_document(self):
        print("Fax not supported in simple printer")
# This is Simple Printer
# It only requires printing functionality
# But due to inheritance we have to forcefully handle other parent functuions in child class
# This is voilation Interface Segreration Principal

mfp = MultiFunctionPrinter()
mfp.print_document()
mfp.scan_document()
mfp.fax_document()

sp = SimplePrinter()
sp.print_document()
sp.scan_document()
sp.fax_document()    