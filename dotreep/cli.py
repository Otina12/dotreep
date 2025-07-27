import argparse
import os
from dotreep.models.folder_composite import FolderComposite
from dotreep.models.file_leaf import FileLeaf


def build_structure(path):
    if os.path.isfile(path):
        return FileLeaf(path)
    
    directory_composite = FolderComposite(path)
    try:
        for entry in os.scandir(path):
            child_path = os.path.join(path, entry.name)
            if entry.is_file():
                directory_composite.add(FileLeaf(child_path))
            elif entry.is_dir():
                directory_composite.add(build_structure(child_path))
    except PermissionError:
        print(f"Cannot access {path}")

    return directory_composite

def main():
    parser = argparse.ArgumentParser(description = "Display a tree view of a directory with sizes.")
    parser.add_argument("path", nargs = "?", default = os.getcwd(), help = "Directory to analyze")
    args = parser.parse_args()

    root = build_structure(args.path)
    root.display_info()
