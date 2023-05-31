from tkinter.simpledialog import askstring
import tkinter.messagebox as messagebox
from tkinter import filedialog
from shutil import rmtree
import shutil
import os

class UtilsController:

    @staticmethod
    def rename(path, table, id, tree):
        """
        Permite cambiar el nombre de una carpeta o archivo en el sistema.
            
        parametros
        ------------
        path: string
            La ruta del archivo o carpeta que se desea renombrar.
        table:
            La tabla Treeview que muestra los elementos del sistema.
        id: str
            El identificador único del elemento en la tabla.
        tree: nary_tree
            El árbol utilizado para organizar los elementos del sistema.
        
         Raises
            ------------
        FileExistsError:
        Se genera si la carpeta que se intenta crear ya existe en el sistema.   
        """
        new_name = askstring("Rename", "Enter new name:")#cuadro de dialogo para ingresar el nombre del archivo o carpeta
        node = tree.find_node(path) #buscar si el archivo o carpeta que se quiere renombrar se encuentra en el arbol

        if new_name and node:
            try:
                if os.path.isfile(path): #verficia si parth corresponde a un archivo
                    old_name, ext = os.path.splitext(path) #extrae el nombre del archivo y su extension
                    #se construye el nuevo nombre udando os.path.join() para combinar el nuevo nombre y la extension
                    new_path = os.path.join(os.path.dirname(path), new_name + ext) 
                    os.rename(path, new_path) #cambia el nombre del archivo
                    #actualiza el nombre del archivo en la visualizancion de la tabla
                    tree.rename_node(path, new_path.replace("\\", "/")) #renombra el nodo correspondiente a la estructura del arbol
                    table.item(id, text=new_name + ext, values=[f"{new_name}{ext}"]) #actualiza el texto del elemento segun el id especificado.
                elif os.path.isdir(path): #verifica si corresponde a una carpeta
                    new_path = os.path.join(os.path.dirname(path), new_name)
                    os.rename(path, new_path)
                    table.item(id, text=new_name, values=[new_name])
                    tree.rename_node(path, new_path)
            except FileExistsError:
                    messagebox.showerror("Error", "The folder/file already exists.")

 
    @staticmethod
    def remove(path, table, id, tree):  
        """
        Permite eliminar un archivo o carpeta en el sistema.
            
        parametros
        -------------
        path: 
            Ruta del archivo o carpeta que se desea eliminar.
        table:
            La tabla Treeview que muestra los elementos el sistema.
        id:
            El identificador del elemento en la tabla.
        tree:
            El arbol utilizado para organizar los elementos en el sistema.

        Error    
        ------------
            En caso de que el la ruta path en el arbol no se encuentre.
        """
        node_find = tree.find_node(path) #busca si path existe en el arbol

        if not node_find:
            messagebox.showerror("Error", "The file or folder could not be deleted")
        else:
            if not os.path.isfile(path): #verifica si no es un archivo, es decir si, si es una carpeta
                if len(os.listdir(path)) == 0: #verifica si la parte esta vacia
                    os.rmdir(path) #elimina la carpeta
                else:
                    rmtree(path) #si no esta vacia, elimina la carpeta con todos sus contenidos
            else:
                os.remove(path) #si path corresponde a un archivo, se elimnina

            table.delete(id) #elimina el elemneto correspondiende te la tabla
            tree.remove_node(path) #elimina el nodo correspondiente del abol
    
    @staticmethod
    def copy_and_paste(path, tree, p_final = None):
        """
        Permite copiar y pegar un archivo o carpeta en el sistema.

        parametros
        -------------
        path:
            Ruta del archivo o carpeta que se desea copiar.
        tree:
            Arbol utilizafo para organizar los elementos del sistema.
        p_final:
            Repreesenta la ruta de destino donde se desea pegar el archivo o carpeta.

        ------------
        Exception:
            Se produce una excepción no especificada durante la copia o pegado del archivo o carpeta.

        """
        #agrega el valor de p_final su esta definido, sino, se muestra un cuadro de dialogo para seleccionar la carpeta
        path_finally = p_final or filedialog.askdirectory(title="Select destination folder") #permite seleccionar una ruta de destino donde se realizará la copia o pegado.

        if path_finally: #si tiene un valor valido
            try:
                if os.path.isfile(path): #verifica si es un archivo
                    shutil.copy(path, path_finally) #copia el archivo ubicado en path a la ruta de destino path_finally
                    tree.add_node(path, path_finally) #agrega un nuevo nodo al árbol para reflejar la nueva ubicación del archivo copiado.
                elif os.path.isdir(path): #verifica si corresponde a una carpeta
                    finally_route =  os.path.join(path_finally, os.path.basename(path)) #combina la ruta de destino con el nombre base de la carpeta
                    shutil.copytree(path, finally_route) 
                    tree.add_node(path, finally_route)
            except Exception as e:
                messagebox.showerror("Error:", str(e))

    @staticmethod
    def move(path, table, id, tree):
        """
        Permite mover una carpeta o archivos del sistema.

        parametros
        ------------
        path: 
            ruta del archivo o carpeta que se desea eliminar.
        table:
            la tabla Treeview que muestra los elementos el sistema.
        id:
            el identificador del elemento en la tabla.
        tree:
            el arbol utilizado para organizar los elementos en el sistema.

        ------------
        Exception:
            Se produce una excepción no especificada durante la copia o pegado del archivo o carpeta.
        """
        # Seleccionar la carpeta de destino mediante un diálogo de selección
        path_finally = filedialog.askdirectory(title="Select destination folder")

        # Verificar si se seleccionó una carpeta de destino
        if path_finally:
            try:
                if os.path.isfile(path):
                    # Mover un archivo a la carpeta de destino
                    shutil.move(path, path_finally)
                    # Actualizar el árbol con el nuevo nodo
                    tree.add_node(path, path_finally)
                elif os.path.isdir(path):
                    finally_route = os.path.join(path_finally, os.path.basename(path))
                    # Mover una carpeta a la carpeta de destino
                    shutil.move(path,finally_route )
                    # Actualizar el árbol con el nuevo nodo
                    tree.add_node(path, finally_route)
                # Eliminar el nodo y el elemento de la tabla correspondientes al archivo o carpeta movido
                tree.remove_node(path)
                table.delete(id) #elimina el elemento de la tabla
            except Exception as e:
                # Mostrar mensaje de error en caso de excepción
                messagebox.showerror("Error:", str(e))