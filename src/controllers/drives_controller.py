import os
from .folders_controller import FoldersController

class DrivesController:
    
    @staticmethod
    def insert_drives(table, valid_drives):
        """
        Inserta las unidades de disco en la tabla 

        parametros
        ------------
        table: ttk.Treeview
            tabla Treeview en donde se insertara los discos
        valid_drives: list
            Una lista de nombres de unidades de disco validadas, dedes A hasta Z
        """
        #Elimina todas las filas existentes en la tabla
        for i in table.get_children():
            table.delete(i) 

        for r in range(len(valid_drives)):
            table.insert(parent='', text='', values = [valid_drives[r]], 
                        index='end')

    @staticmethod
    def find_valid_drives(drives, valid_drives):
        """
        Busca las unidades de disco validas en base a una lista de nombres de discos proporcionada
        y las agrega en la lista 'valid_drives'.
        
        parametros
        -------------
        drives:
            Lista de nombre de disco de unidades validadas, desde la A hasta la Z.
        valid_drives: list
            Lista en donde se agregaran los nombres de las unidades de disco validas encontradas.
        """
        
        for drive in drives:
            if os.path.exists(drive):#verifica si cada unidades de disco existe en el sistema
                valid_drives.append(drive)

    @staticmethod
    def open_drive(base_path, table, main_table, tree):
        """
        permite abrir los archivos que se encuentren en la unidad de disco seleccionada.

            parametros
            -------------
            base_path : str
                Ruta base que representa la unidad de disco seleccionada.
            table : ttk.Treeview
                Tabla Treeview que muestra las unidades de disco.
            main_table : ttk.Treeview
                Tabla Treeview principal que muestra los archivos y carpetas del disco.
            tree : NaryTree
                Árbol n-ario que representa la estructura de archivos y carpetas.

            return:
                None
        """
        #Si no hay ninguna selección, se detiene la ejecución del método.
        if not table.selection():
            return

        FoldersController.insert_folders(base_path, main_table, tree)#inserta las carpetas contenidas en el disco
