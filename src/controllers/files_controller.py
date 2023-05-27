import os
from .context_menu_controller import MenuController
from tkinter.simpledialog import askstring
class FilesController:

    @staticmethod
    def insert_files(table, path, tree, menu):
        for i in table.get_children():
            table.delete(i)

        current_route = path['text']

        files = os.listdir(current_route)
        children = tree.find_node(current_route).children

        if len(children) == 0:
            for file in files:
                tree.add_node(f"{current_route}/{file}", current_route)

        for r in range(len(children)):
            name = os.path.basename(children[r].data)             
            table.insert(parent='', text='', index='end', values=[name])

        for item in table.get_children():
            table.item(item, tags=item)
            table.tag_bind(item, '<Button-3>', lambda e: MenuController.open(e, menu, table, current_route))

    @staticmethod
    def create_file (path, tree, table):
        new_name = askstring("Name", "Enter new name:")
        full_path = ''
        if new_name: 
            try:
                if path['text'] == 'C://':
                    full_path = f"{path['text']}{new_name}.txt"
                else:
                    full_path = f"{path['text']}/{new_name}.txt"

                with open(full_path, 'w') as archivo:
                    pass  
                table.insert(parent='', text='', index='end', values=[new_name + ".txt"])
                tree.add_node(full_path, path['text'])
            except IOError:
                print(f"No se pudo crear el archivo en la ruta: {full_path}")
