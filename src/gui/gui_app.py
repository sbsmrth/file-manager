import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttkb
from src.controllers.drives_controller import DrivesController
from src.controllers.folders_controller import FoldersController
from src.controllers.files_controller import FilesController
from src.controllers.context_menu_controller import MenuController
from src.controllers.utils_controller import UtilsController
from src.nary_tree import NaryTree
from src.nary_tree_node import NaryTreeNode


class FileExplorer():
    """
        Clase que representa un explorador de archivos.

        Atributos:
        ----------
        tree: NaryTree
            El árbol utilizado para organizar los elementos del sistema.
        last_path: dict
            El último directorio seleccionado en el explorador.
        window: tkinter.Tk
            La ventana principal de la aplicación.
    """
    def __init__(self):
        """
            inicializa una nueva instancia de la clase FileExplorer
            configura la interfaz del usuario y los atributos necesarios para el funcionamiento del explorador de archivos
        """
        self.tree = NaryTree(NaryTreeNode('C://')) #se crea el objeto NaryTree con el nodo raiz
        
        self.last_path = {'text': self.tree.root.data}  # Almacena la última ruta seleccionada en el explorador de archivos.

        self.window = ttkb.Window(themename='darkly')  # Crea una nueva ventana utilizando ttkbootstrap con el tema 'darkly'.
        self.window.attributes('-fullscreen', True)  # Establece la ventana en modo de pantalla completa.
        self.window.title('File Explorer')  # Establece el título de la ventana como 'File Explorer'.

        self.style = ttk.Style(self.window)  # Crea un objeto de estilo asociado a la ventana.
        self.style.configure('Treeview', font=('Bold',13))  # Configura el estilo para los elementos de tipo 'Treeview'.

        self.user_win_width = self.window.winfo_screenwidth()  # Obtiene el ancho de la ventana de usuario en píxeles.
        self.left_table_width = int(self.user_win_width * 0.2)  # Calcula el ancho deseado para la tabla izquierda.
        self.main_table_width = int(self.user_win_width * 0.8)  # Calcula el ancho deseado para la tabla principal.

        self.drives = ['A://', 'B://', 'C://',
                'D://', 'E://', 'F://',
                'G://', 'H://', 'I://',
                'J://', 'K://', 'L://',
                'M://', 'N://', 'O://',
                'P://', 'Q://', 'R://',
                'S://', 'T://', 'U://', 
                'V://', 'W://', 'X://',
                'Y://', 'Z://']

        self.valid_drives = []

        self.context_menu = tk.Menu(self.window, tearoff=False)  # Crea un menú contextual utilizando el widget tk.Menu asociado a la ventana.
        self.context_menu.add_command(label='Rename', command=lambda: UtilsController.rename(MenuController.route, self.main_table, MenuController.id, self.tree)) 
        self.context_menu.add_command(label='Delete', command=lambda: UtilsController.remove(MenuController.route, self.main_table, MenuController.id, self.tree))  # Agrega un comando al menú contextual con la etiqueta 'Delete' que llama a la función remove().
        self.context_menu.add_command(label='Copy', command=lambda: UtilsController.copy_and_paste(MenuController.route, self.tree))  # Agrega un comando al menú contextual con la etiqueta 'Copy' que llama a la función copy_and_paste().
        self.context_menu.add_command(label='Move', command=lambda: UtilsController.move(MenuController.route, self.main_table, MenuController.id, self.tree))  # Agrega un comando al menú contextual con la etiqueta 'Move' que llama a la función move().

        self.top_utils_menu = ttkb.Menu()  # Crea un menú superior utilizando el widget ttkb.Menu.
        self.down_utils_menu = ttkb.Menu(self.top_utils_menu, tearoff=False)  # Crea un submenú dentro del menú superior
        self.utils_folder_icon = tk.PhotoImage(file="./src/assets/folder.png")  # Carga una imagen para el icono de carpeta.
        self.utils_file_icon = tk.PhotoImage(file="./src/assets/file.png")  # Carga una imagen para el icono de archivo.
        self.down_utils_menu.add_command(label="Folder", accelerator="Ctrl+N", command=lambda: FoldersController.create_folder(self.main_table, self.last_path, self.tree), image=self.utils_folder_icon,
                                         compound=tk.LEFT)  # Agrega un comando al submenú con la etiqueta 'Folder', llama a la función create_folder() y muestra el icono de carpeta junto al texto del comando.
        self.down_utils_menu.add_command(label="File", command=lambda: FilesController.create_file(self.last_path, self.tree, self.main_table), image=self.utils_file_icon,
                                         compound=tk.LEFT)  # Agrega un comando al submenú con la etiqueta 'File', llama a la función create_file() y muestra el icono de archivo junto al texto del comando.
        self.window.bind_all("<Control-n>", lambda: FoldersController.create_folder(self.main_table, self.last_path, self.tree))  # Asocia la combinación de teclas Ctrl+N a la función create_folder().
        self.down_utils_menu.add_separator()  # Agrega un separador en el submenú.
        self.down_utils_menu.add_command(label="Exit", command=self.window.destroy)  # Agrega un comando al submenú con la etiqueta 'Exit' que cierra la ventana principal.
        self.top_utils_menu.add_cascade(menu=self.down_utils_menu, label="New")  # Agrega el submenú como una cascada en el menú superior con la etiqueta 'New'.
        self.window.config(menu=self.top_utils_menu)  # Configura el menú superior en la ventana principal.

        self.side_table = ttk.Treeview(self.window)  # Hace referencia al widget Treeview llamado side_table.

        self.side_table['column'] = ['Drives']  # Define la columna del Treeview con el nombre 'Drives'.
        self.side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)  # Configura la columna '#0' del Treeview para que tenga un ancho de 0 y no se estire.
        self.side_table.column('Drives', anchor=tk.W,  width=self.left_table_width)  # Configura la columna 'Drives' del Treeview para que tenga un ancho igual al valor de la variable self.left_table_width.
        self.side_table.heading('Drives', text='Drives', anchor=tk.W)  # Establece la etiqueta de encabezado de la columna 'Drives' del Treeview como 'Drives' y la alinea a la izquierda (anchor=tk.W).


        self.side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)  # Empaqueta y coloca el Treeview side_table en el lado izquierdo de la ventana, anclado a la izquierda (anchor=tk.W) y se expande en el eje Y (fill=tk.Y).

        self.side_table.bind('<<TreeviewSelect>>', lambda e: DrivesController.open_drive(self.last_path, self.side_table, self.main_table, self.tree))  # Vincula el evento '<<TreeviewSelect>>' del Treeview side_table a una función lambda que llama al método open_drive.
        self.main_table = ttk.Treeview(self.window)  # Crea un nuevo Treeview llamado main_table.
        self.main_table['column'] = ['Files']  # Define la columna del Treeview con el nombre 'Files'.
        self.main_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)  # Configura la columna '#0' del Treeview para que tenga un ancho de 0 y no se estire.
        self.main_table.column('Files', anchor=tk.W, width=self.main_table_width)  # Configura la columna 'Files' del Treeview para que tenga un ancho igual al valor de la variable self.main_table_width.
        self.main_table.heading('Files', text='File', anchor=tk.W)  # Establece la etiqueta de encabezado de la columna 'Files' del Treeview como 'File' y la alinea a la izquierda (anchor=tk.W).
        self.main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)  # Empaqueta y coloca el Treeview main_table en el lado izquierdo de la ventana, anclado a la izquierda (anchor=tk.W) y se expande en el eje Y (fill=tk.Y).
        self.main_table.bind('<<TreeviewSelect>>', lambda e: FoldersController.open_folder(self.main_table, self.tree, self.context_menu, self.last_path))  # Vincula el evento '<<TreeviewSelect>>' del Treeview main_table a una función lambda que llama al método open_folder

        DrivesController.find_valid_drives(self.drives, self.valid_drives)  # Llama al método find_valid_drives 

        DrivesController.insert_drives(self.side_table, self.valid_drives)  # Llama al método insert_drives


    def run(self):
        """
            Ejecuta el explorador de archivos, es decir que inicia la aplicacion y muestra la ventana principal
        """
        self.window.mainloop()