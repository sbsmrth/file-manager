import os
import tkinter.messagebox as messagebox
from tkinter.simpledialog import askstring

class FilesController:

    @staticmethod
    def rename_file(path, table, id):
        try:
            if os.path.isfile(path):
                new_name = askstring("Rename file.", "Enter new file name:")
                if new_name:
                    old_name, ext = os.path.splitext(path)
                    new_path = os.path.join(os.path.dirname(path), new_name + ext)
                    os.rename(path, new_path)
                    table.item(id, text=new_name + ext, values=(new_name + ext,))
        except Exception:
            messagebox.showerror("Error", "The action could not be completed")

    @staticmethod
    def remove_file(path, table, id):
        try:
            if os.path.isfile(path):
                os.remove(path)
                table.delete(id)
        except Exception:
            messagebox.showerror("Error", "The file cannot be deleted")

       









