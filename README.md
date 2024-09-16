
# Odoo Module Dependency Tree Generator

This Python script is designed to analyze the dependencies between Odoo modules by parsing their `__manifest__.py` files. It then generates and displays a tree structure representing the dependencies between modules.

## Features
- Scans the selected Odoo `addons` folder for `__manifest__.py` files.
- Extracts module dependencies from the manifests.
- Builds and displays a tree structure showing the dependency relationships between modules.
- Provides two ways to input the folder path: manual entry or file selector dialog.

## Requirements

- Python 3.x
- Required libraries: `anytree`, `tkinter`

Install the required libraries using pip:

```bash
pip install anytree
```

## How to Use

1. **Run the Script**: Execute the script in a terminal or command prompt:

    ```bash
    python main.py
    ```

2. **Select Addons Path**:
    - You will be prompted to manually input the path to the `addons` folder or select it using a file selector.
  
    - Option 1: Manually enter the folder path.
    - Option 2: Use the file dialog to select the folder.

3. **View the Dependency Tree**:
    - The script will parse the `__manifest__.py` files, build a dependency tree, and print the tree structure to the console.

## Example

```
Enter the addons folder path: /path/to/your/addons

module1
├── module2
│   └── module3
└── module4
```

## How It Works

1. **find_manifest_files(addons_path)**: 
    - Walks through the `addons` folder and finds all `__manifest__.py` files.

2. **parse_manifest_file(file_path)**: 
    - Parses each manifest file to retrieve the module name and its dependencies.

3. **build_dependency_tree(manifest_files)**: 
    - Builds a tree structure showing the relationships between modules based on their dependencies.

4. **create_tree_nodes(tree, all_modules)**:
    - Converts the module tree into a structure that can be displayed using the `anytree` library.

5. **display_tree(root_nodes)**:
    - Displays the module dependency tree in a human-readable format.
