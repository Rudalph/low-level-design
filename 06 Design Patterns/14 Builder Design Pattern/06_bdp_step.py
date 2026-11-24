
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (
            f"CPU: {self.cpu}\n"
            f"RAM: {self.ram}\n"
            f"Storage: {self.storage}\n"
            f"GPU: {self.gpu}"
        )


class CPUBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return RAMBuilder(self.computer)


class RAMBuilder:
    def __init__(self, computer):
        self.computer = computer

    def set_ram(self, ram):
        self.computer.ram = ram
        return StorageBuilder(self.computer)


class StorageBuilder:
    def __init__(self, computer):
        self.computer = computer

    def set_storage(self, storage):
        self.computer.storage = storage
        return GPUBuilder(self.computer)


class GPUBuilder:
    def __init__(self, computer):
        self.computer = computer

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


# Usage
builder = CPUBuilder()

gaming_pc = (
    builder
    .set_cpu("Intel i9")
    .set_ram("32 GB")
    .set_storage("1 TB SSD")
    .set_gpu("NVIDIA RTX")
    .build()
)

print(gaming_pc)
