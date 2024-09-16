import os
import ast
from collections import defaultdict
from anytree import Node, RenderTree
from tkinter import Tk
from tkinter.filedialog import askdirectory


def find_manifest_files(addons_path):
    manifest_files = []
    for root, dirs, files in os.walk(addons_path):
        if '__manifest__.py' in files:
            manifest_files.append(os.path.join(root, '__manifest__.py'))
    return manifest_files


def parse_manifest_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    manifest = ast.literal_eval(content)
    module_name = os.path.basename(os.path.dirname(file_path))
    dependencies = manifest.get('depends', [])
    return module_name, dependencies


def build_dependency_tree(manifest_files):
    tree = defaultdict(list)
    all_modules = set()
    for file_path in manifest_files:
        module, dependencies = parse_manifest_file(file_path)
        all_modules.add(module)
        for dep in dependencies:
            tree[dep].append(module)
            all_modules.add(dep)
    return tree, all_modules


def create_tree_nodes(tree, all_modules):
    nodes = {module: Node(module) for module in all_modules}
    for module, dependencies in tree.items():
        for dep in dependencies:
            nodes[dep].parent = nodes[module]
    return nodes


def display_tree(root_nodes):
    for root in root_nodes:
        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")


def get_addons_path():
    # Initialize Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window
    addons_path = askdirectory(title="Select the addons folder")
    root.destroy()  # Close the Tkinter window
    return addons_path


if __name__ == '__main__':
    choice = input("Do you want to (1) enter the path manually or (2) open the file selector? Enter 1 or 2: ").strip()
    addons_path = ''

    if choice == '1':
        addons_path = input("Enter the addons folder path: ").strip()
    elif choice == '2':
        addons_path = get_addons_path()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        exit(1)

    if addons_path and os.path.isdir(addons_path):
        manifest_files = find_manifest_files(addons_path)
        if manifest_files:
            dependency_tree, all_modules = build_dependency_tree(manifest_files)
            nodes = create_tree_nodes(dependency_tree, all_modules)

            root_nodes = [node for node in nodes.values() if node.is_root]
            display_tree(root_nodes)
        else:
            print("No manifest files found in the selected folder.")
    else:
        print("Invalid or no folder selected.")
