class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer
    
class ComputerDirector:

    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return (
            self.builder
            .set_cpu("Intel i9")
            .set_ram("32 GB")
            .set_storage("1 TB SSD")
            .set_gpu("NVIDIA RTX")
            .build()
        )
        
builder = ComputerBuilder()

director = ComputerDirector(builder)

gaming_pc = director.build_gaming_pc()

'''You don't always need a Director.'''