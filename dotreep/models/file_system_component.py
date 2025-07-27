from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def display_info(self, indent = 0, is_last = True):
        pass
