from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def display_content(self):
        pass
    
class ImageDisplay(Display):
    def __init__(self):
        print('-- Performing Heavy Computational Task --')
        
    def display_content(self):
        print('Diaplaying the image')
        
class ImageDisplayProxy(Display):
    def __init__(self):
        self.image_display = None
        
    def display_content(self):
        if self.image_display == None:
            self.image_display = ImageDisplay()
        self.image_display.display_content()

client = ImageDisplayProxy()
client.display_content()
    