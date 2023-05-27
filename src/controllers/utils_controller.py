from tkinter.simpledialog import askstring
import tkinter.messagebox as messagebox
from tkinter import filedialog
from shutil import rmtree
import shutil
import os

class UtilsController:

    @staticmethod
    def rename(path, table, id, tree):
        new_name = askstring("Rename", "Enter new name:")
        node = tree.find_node(path)

        if new_name and node:
            if os.path.isfile(path):
                old_name, ext = os.path.splitext(path)
                new_path = os.path.join(os.path.dirname(path), new_name + ext)
                os.rename(path, new_path)

                table.item(id, text=new_name + ext, values=[f"{new_name}{ext}"])
                tree.rename_node(path, new_path.replace("\\", "/"))
            elif os.path.isdir(path):
                new_path = os.path.join(os.path.dirname(path), new_name)
                os.rename(path, new_path)
                table.item(id, text=new_name, values=[new_name])
                tree.rename_node(path, new_path)

    @staticmethod
    def remove(path, table, id, tree):
        node_find = tree.find_node(path)

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
            tree.remove_node(path)
    
    @staticmethod
    def copy_and_paste(path, tree, p_final = None):
        path_finally = p_final or filedialog.askdirectory(title="Select destination folder")

        if path_finally:
            try:
                if os.path.isfile(path):
                    shutil.copy(path, path_finally)
                    tree.add_node(path, path_finally)
                elif os.path.isdir(path):
                    shutil.copytree(
                        path, os.path.join(path_finally, os.path.basename(path))
                    )
                    tree.add_node(
                        path, os.path.join(path_finally, os.path.basename(path))
                    )

            except Exception as e:
                messagebox.showerror("Error:", str(e))

    @staticmethod
    def move(path, table, id, tree):
        path_finally = filedialog.askdirectory(title="Select destination folder")

        if path_finally:
            try:
                if os.path.isfile(path):
                    shutil.move(path, path_finally)
                    tree.add_node(path, path_finally)
                elif os.path.isdir(path):
                    shutil.move(
                        path, os.path.join(path_finally, os.path.basename(path))
                    )
                    tree.add_node(
                        path, os.path.join(path_finally, os.path.basename(path))
                    )
                tree.remove_node(path)
                table.delete(id)
            except Exception as e:
                messagebox.showerror("Error:", str(e))
