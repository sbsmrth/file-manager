from src.nary_tree import NaryTree
from src.nary_tree_node import NaryTreeNode
from src.controllers.folders_controller import FoldersController
import tkinter as tk
from tkinter import ttk

import os

def test_insert_folders():
    window = tk.Tk()
    main_table = ttk.Treeview(window)
    main_table['column'] = ['Files']
    tree = NaryTree(NaryTreeNode('C://'))
    number_files = len(os.listdir(tree.root.data))
    path_dict = {'text': tree.root.data}

    FoldersController.insert_folders(path_dict, main_table, tree)
    children_len = len(tree.find_node(tree.root.data).children)
    assert children_len == number_files # verificar si fueron añadidos al arbol
    assert len(main_table.get_children()) == number_files # verificar si fueron añadidos a la tabla
