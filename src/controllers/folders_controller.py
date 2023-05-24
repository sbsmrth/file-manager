import os
from .files_controller import FilesController
from tkinter.simpledialog import askstring

class FoldersController:

    @staticmethod
    def insert_folders(path, table, tree):

        for item in table.get_children():
            table.delete(item)

        path['text'] = 'C://'
        new_path = path['text']


        folders = os.listdir(new_path)

        node = tree.find_node(new_path)
        if len(node.children) == 0:
            for file in folders:
                tree.add_node(f"{new_path}{file}", new_path)

        node_children = node.children

        for r in range(len(node_children)):
            name = os.path.basename(node_children[r].data)
            table.insert(parent='', text='', values=[name], index='end')

    @staticmethod
    def open_folder(table, tree, menu, path):
    
        if not table.selection():
            return
        
        row_text = table.item(table.selection()[0])['values'][0]
        
        if path['text'] == tree.root.data:
            path['text'] +=  row_text
        else:
            path['text'] +=  f"/{row_text}"

        if os.path.isdir(path['text']):
            FilesController.insert_files(table, path, tree, menu)
        else:
            os.system('"%s"' % path['text'])

    @staticmethod
    def create_folder (table, path, tree):
        new_name = askstring("Name", "Enter new name:")
        full_path = ''

        if new_name:
            try:
                if path['text'] == 'C://':
                    full_path = f"{path['text']}{new_name}"
                    os.mkdir(full_path)
                else:
                    full_path = f"{path['text']}/{new_name}"
                    os.mkdir(full_path)
                table.insert(parent='', text='', index='end', values=[new_name])
                tree.add_node(full_path, path['text'])
            except FileExistsError:
                print("The folder already exists.")
            except OSError as e:
                print(f"Se produjo un error al crear la carpeta: {e}")
