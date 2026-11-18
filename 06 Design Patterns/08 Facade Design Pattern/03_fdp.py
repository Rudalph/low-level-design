class Client:
    def __init__(self, facade):
        self.facade = facade
        
    def start_computer(self):
        self.facade.start_computer()
        
class ComputerFacade:
    def __init__(self, cpu, memory, hard_drive, operating_system):
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive
        self.operating_system = operating_system
    
    def start_computer(self):
        self.cpu.start_cpu()
        self.memory.start_memory()
        self.hard_drive.start_hard_drive()
        self.operating_system.start_operating_system()
        
class CPU:
    def start_cpu(self):
        print('Starting CPU')

class Memory:
    def start_memory(self):
        print('Starting Memory')
        
class HardDrive:
    def start_hard_drive(self):
        print('Starting Hard Drive')
        
class OperatingSystem:
    def start_operating_system(self):
        print('Starting Operating System')
        
cpu = CPU()
memory = Memory()
hard_drive = HardDrive()
operating_system = OperatingSystem()

computer_facade = ComputerFacade(cpu, memory, hard_drive, operating_system)

client = Client(computer_facade)
client.start_computer()