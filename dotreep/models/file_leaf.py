import os
from dotreep.models.file_system_component import FileSystemComponent

class FileLeaf(FileSystemComponent):
    def get_name(self):
        return os.path.basename(self.path)

    def get_size(self):
        return os.path.getsize(self.path)

    def display_info(self, indent = "", is_last = True):
        connector = "└── " if is_last else "├── "
        name = self.get_name()
        print(f"{indent}{connector}{name} | Size: {self.get_size()} bytes")