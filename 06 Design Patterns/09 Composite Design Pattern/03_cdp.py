from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    def __init__(self, name):
        self.item_name = name
        
    @abstractmethod
    def ls(self):
        pass
    
    @abstractmethod
    def open_all(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
class FileItem(FileSystemItem):
    def ls(self):
        return 'Operation Not Applicable'
    
    def open_all(self):
        print(self.item_name)
    
    def get_size(self):
        return len(self.item_name)
    
    def get_name(self):
        return self.item_name
    
class FolderItem(FileSystemItem):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
        
    def add_child(self, item):
        self.children.append(item)
    
    def ls(self):
        for child in self.children:
            print(child.get_name())
    
    def open_all(self):
        print(self.item_name)
        for child in self.children:
            child.open_all()

    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        return size

    def get_name(self):
        return self.item_name
    
'''
root
    |- File1.txt
    |- File2.txt
    |- Core
        |- File3.txt
        |- File4.txt
    |- User
        |- File5.txt
'''

root = FolderItem('root')
file1 = FileItem('file1.txt')
file2 = FileItem('file2.txt')

root.add_child(file1)
root.add_child(file2)

core = FolderItem('Core')
file3 = FileItem('file3.txt')
file4 = FileItem('file4.txt')

core.add_child(file3)
core.add_child(file4)
root.add_child(core)

user = FolderItem('user')
file5 = FileItem('file5.txt')

user.add_child(file5)
root.add_child(user)


root.ls()
root.open_all()
print(root.get_size())