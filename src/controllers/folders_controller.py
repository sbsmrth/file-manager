import os
from .files_controller import FilesController
from tkinter.simpledialog import askstring
from tkinter import messagebox

class FoldersController:

    @staticmethod
    def insert_folders(path, table, tree):
        """
        Insertar las carpetas en la tabla.

        parametros
        ------------
        path: str
            ruta de la  carpeta que se desea insetar.
        table: tkinter.ttk.Treeview
            la tabla Treeview que muestra los elementos el sistema.
        tree: NaryTree
            Arbol utilizado para organizar los elementos en el sistema.
        """

        for item in table.get_children():
            table.delete(item) #elimina los elementos existente en la tabla

        path['text'] = 'C://' #establece la ruta actual
        new_path = path['text'] #obtiene la nueva ruta de la carpeta

        folders = os.listdir(new_path) #Obtiene una lista de las carpetas en la ruta new_path

        node = tree.find_node(new_path) #Encuentra el nodo correspondiente a new_path
        if len(node.children) == 0: #en caso de que el nodo no tenga hijos
            for file in folders:
                tree.add_node(f"{new_path}{file}", new_path) #agrega las carpetas al arbol

        node_children = node.children

        for r in range(len(node_children)):
            name = os.path.basename(node_children[r].data) #obtiene el nombre base de la ruta utilizando 
            table.insert(parent='', text='', values=[name], index='end') #inserta una nueva fila en la tabla (table) con el nombre de la carpeta (name) 

    @staticmethod
    def open_folder(table, tree, menu, path):
        """
        Abre la carpeta del elemento seleccionado en la tabla.

        parametros
        -------------
        path: str
            Ruta de la carpeta que se desea abrir.
        table: tkinter.ttk.Treeview
            Tabla Treeview que muestra los elementos el sistema
        tree: NaryTree
            Arbol utilizado para organizar los elementos en el sistema

        return
        --------------
        None
        """
    
        if not table.selection():#verificar sino se ha seleccionado ningun elemento en la tabla
            return
        
        #obtiene el texto de la primera columna del elemento seleccionado en la tabla
        row_text = table.item(table.selection()[0])['values'][0]
         # Verificar si la ruta actual es la raíz del árbol
        if path['text'] == tree.root.data:
            # Agregar el texto de row_text al texto actual de path
            path['text'] += row_text
        else:
            # Agregar una barra diagonal y el texto de row_text al texto actual de path
            path['text'] += f"/{row_text}"
        
        # Verificar si la ruta actual corresponde a un directorio existente
        if os.path.isdir(path['text']):
            # Insertar los archivos en la tabla, utilizando FilesController.insert_files
            FilesController.insert_files(table, path, tree, menu)
        else:
            # Si no es un directorio, abrir la ruta en el sistema operativo
            os.system('"%s"' % path['text'])
            path['text'] = os.path.dirname(path['text'])

    @staticmethod
    def create_folder (table, path, tree):
        """
        Permite crear carpetas.

        parametros
        -----------
        path:  str
            Ruta del carpeta que se desea crear.
        table: tkinter.ttk.Treeview
            La tabla Treeview que muestra los elementos en el sistema.
        tree: NaryTree
            Arbol utilizado para organizar los elementos en el sistema.

        Raises
            ------------
        FileExistsError:
        Se genera si la carpeta que se intenta crear ya existe en el sistema.
        OSError:
        Se genera si ocurre un error al intentar crear la carpeta, como permisos insuficientes o una ruta inválida.
        """
        new_name = askstring("Name", "Enter new name:") #solicitar al usuari que ingrese en nuevo nombre de la carpeta 
        full_path = '' #se inicializa

        if new_name: #verifica que se haya ingresado un nombre valido
            try:
                #se empieza a contruir la ruta completa
                if path['text'] == 'C://': #en caso de que path en la posisicion 'text' sea igual a 'C://'
                    full_path = f"{path['text']}{new_name}" #full_paht sera la ruta que hay en path, concatenada con el nombre del archivo
                    os.mkdir(full_path)#crea una nueva capeta
                else:
                    full_path = f"{path['text']}/{new_name}"
                    os.mkdir(full_path)

                # Insertar el nombre de la nueva carpeta en la tabla
                table.insert(parent='', text='', index='end', values=[new_name])
                # Agregar el nuevo nodo al árbol
                tree.add_node(full_path, path['text'])
            except FileExistsError:
                messagebox.showerror("error", "The folder already exists.")
            except OSError as e:
                messagebox.showerror("error", f"The folder can't be created: {e}")
