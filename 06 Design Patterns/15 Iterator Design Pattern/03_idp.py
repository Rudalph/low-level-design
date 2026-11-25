from abc import ABC, abstractmethod

# Iterator
class Iterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Concrete Iterator - How to traverse an array logic (We can implement for linkedlist, tree, map etc.)
class MusicIterator(Iterator):

    def __init__(self, songs):
        self.songs = songs
        self.position = 0

    def has_next(self):
        return self.position < len(self.songs)

    def next(self):
        if self.has_next():
            song = self.songs[self.position]
            self.position += 1
            return song

        raise StopIteration
    
# Iterable
class Playlist(ABC):

    @abstractmethod
    def create_iterator(self):
        pass

# Concrete Iterable - This is the object that we want to traverse
class MusicPlaylist(Playlist):

    def __init__(self):
        self.songs = [
            "Song A",
            "Song B",
            "Song C",
            "Song D"
        ]

    def create_iterator(self):
        return MusicIterator(self.songs)
    

playlist = MusicPlaylist()

iterator = playlist.create_iterator()

