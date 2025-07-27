import os
from dotreep.models.file_system_component import FileSystemComponent

class FolderComposite(FileSystemComponent):
    def __init__(self, path):
        super().__init__(path)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_name(self):
        return os.path.basename(self.path) or self.path

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def display_info(self, indent = "", is_last = True):
        connector = "└── " if is_last else "├── "
        name = self.get_name()
        print(f"{indent}{connector}{name} | Size: {self.get_size()} bytes")

        sorted_children = sorted(self.children, key = lambda c: c.get_size(), reverse = True)
        new_indent = indent + ("    " if is_last else "│   ")

        for i, child in enumerate(sorted_children):
            is_last = (i == len(sorted_children) - 1)
            child.display_info(new_indent, is_last)

