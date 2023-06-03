import os
from .context_menu_controller import MenuController
from tkinter.simpledialog import askstring
from tkinter import messagebox
class FilesController:

    @staticmethod
    def insert_files(table, path, tree, menu):
        """
            Metodo estatico que permite insertar archivos

            parametros
            ------------
            table:
                la tabla Treeview que muestra los elementos el sistema
            path: 
                ruta del archivo o carpeta que se desea eliminar
            tree:
                el arbol utilizado para organizar los elementos en el sistema
            menu:

        """
       # Eliminar todos los elementos actuales en la tabla
        for i in table.get_children():
            table.delete(i)

        # Obtener la ruta actual
        current_route = path['text']

        # Obtener la lista de archivos en la ruta actual
        files = os.listdir(current_route)

        # Obtener los hijos del nodo correspondiente a la ruta actual en el árbol
        children = tree.find_node(current_route).children

        # Agregar los archivos a la estructura del árbol si no hay hijos
        if len(children) == 0:
            for file in files:
                tree.add_node(f"{current_route}/{file}", current_route)

        # Insertar los nombres de los archivos en la tabla
        for r in range(len(children)):
            name = os.path.basename(children[r].data)
            table.insert(parent='', text='', index='end', values=[name])

        # Asignar etiquetas y enlaces de menú contextual a cada elemento de la tabla
        for item in table.get_children():
            table.item(item, tags=item)
            table.tag_bind(item, '<Button-3>', lambda e: MenuController.open(e, menu, table, current_route))

    @staticmethod
    def create_file (path, tree, table, menu):
        """
            Metodo estatico que permite crear archivos

            parametros
            ------------
            path: str
                ruta del archivo o carpeta que se desea eliminar
            tree: NaryTree
                el arbol utilizado para organizar los elementos en el sistema           
            table: tkinter.ttk.Treeview
                la tabla Treeview que muestra los elementos el sistema
            
        """
        # Solicitar al usuario el nombre del nuevo archivo
        new_name = askstring("Name", "Enter new name:")
        raw_name, ext = os.path.splitext(new_name) #extrae el nombre del archivo y su extension

        if not ext: #sino no hay una extension
            ext = '.txt'

        # Inicializar la variable full_path
        full_path = ''

        # Verificar si se ha ingresado un nombre válido
        if new_name : 
            try:
                 # Construir la ruta completa del nuevo archivo con la extension
                 if path['text'] == 'C://':
                     full_path = f"{path['text']}{raw_name}{ext}"
                 else:
                     full_path = f"{path['text']}/{raw_name}{ext}"

                 # Crear el archivo vacío en la ruta completa
                 with open(full_path, 'w') as archivo:
                     pass  

                 # Insertar el nombre del nuevo archivo en la tabla
                 row = table.insert(parent='', text='', index='end', values=[raw_name + ext])
                 table.item(row, tags=row)
                 table.tag_bind(row, '<Button-3>', lambda e: MenuController.open(e, menu, table, path['text']))

                 # Agregar el nuevo nodo al árbol
                 tree.add_node(full_path, path['text'])
                
            except IOError:
                messagebox.showerror("Error", f"No se pudo crear el archivo en la ruta: {full_path}")