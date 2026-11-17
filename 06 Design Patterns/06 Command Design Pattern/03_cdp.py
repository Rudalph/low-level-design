'''Smart Home Automation'''

from abc import ABC, abstractmethod

class RemoteControl:
    def __init__(self, cmd):
        self.command = cmd
        
    def press_button(self):
        self.command.execute()
        self.command.undo()
    
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
    
class LightCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()
        
class Light:
    def on(self):
        print('Lights turned on')
    
    def off(self):
        print('Lights turned off')
        
light = Light()
command = LightCommand(light)
remote = RemoteControl(command)
remote.press_button()