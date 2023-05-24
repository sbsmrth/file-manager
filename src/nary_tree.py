
from src.nary_tree_node import NaryTreeNode
import os
import tkinter.messagebox as messagebox
from tkinter.simpledialog import askstring
from tkinter import filedialog
import shutil
import tkinter as tk
from shutil import rmtree

class NaryTree:
    def __init__(self, root) :
            self.root = root
            
    def add_node (self, data, parent=None):
            new_node = NaryTreeNode(data)
            if parent is None:
                self.root = new_node
            else:
                for node in self._find_node(parent, self.root):
                    node.children.append(new_node)
        
    def _find_node(self, data, current_node):
            nodes = []
            if current_node.data == data:
                nodes.append(current_node)
            for child in current_node.children:
                nodes += self._find_node(data, child)
            return nodes

    def find_node (self, data): 
            nodes= self._find_node(data, self.root)
            if nodes :
                return nodes[0]
            return None
    
    def _print_node (self, root):
        print(root.data)
        for nodo in root.children:
            if nodo is not None:
                 self._print_node(nodo)
        
    def print_node (self):
            self._print_node(self.root)

    def rename_node(self, path, table, id):
        node_find = self.find_node(path)

        if not node_find:   
            messagebox.showerror("Error", "The action could not be completed")
        else: 
            new_name = askstring("Rename", "Enter new name:")
            if new_name:
                if os.path.isfile(path):
                    dir_name = os.path.dirname(path)
                    old_name, ext = os.path.splitext(path)
                    new_path = os.path.join(dir_name, new_name + ext)
                    os.rename(path, new_path)
                    table.item(id, text=new_name, values=(new_name + ext))
                    node_find.data = new_path.replace("\\", "/")
                elif os.path.isdir(path):
                    new_path = os.path.join(os.path.dirname(path), new_name)
                    os.rename(path, new_path)
                    table.item(id, text=new_name, values=(new_name))
                    node_find.data = new_path

    def remove_node(self, path, table, id):
        node_find = self.find_node(path)

        if not node_find:
            messagebox.showerror("Error", "The file or folder could not be deleted")
        else:
            if not os.path.isfile(path):
                if len(os.listdir(path)) == 0:
                    os.rmdir(path)
                else:
                    rmtree(path)
            else:
                os.remove(path)
            table.delete(id)
    
    def copy_and_paste(self, path, table):
        path_finally = filedialog.askdirectory(title="Seleccionar carpeta de destino")

        if path_finally:
            try:
                if os.path.isfile(path):
                    shutil.copy(path, path_finally)
                    self.add_node(path, path_finally)
                elif os.path.isdir(path):
                    shutil.copytree(path, os.path.join(path_finally, os.path.basename(path)))
                    self.add_node(path, os.path.join(path_finally, os.path.basename(path)))

            except Exception as e:
                messagebox.showerror("Error:", str(e))
    
    def move (self, path, table, id):
        path_finally = filedialog.askdirectory(title="Seleccionar carpeta de destino")

        if path_finally:
            try:
                if os.path.isfile(path):
                    shutil.move(path, path_finally)
                    self.add_node(path, path_finally)
                elif os.path.isdir(path):
                    shutil.move(path, os.path.join(path_finally, os.path.basename(path)))
                    self.add_node(path, os.path.join(path_finally, os.path.basename(path)))
                table.delete(id)
            except Exception as e:
                messagebox.showerror("Error:", str(e))
    



