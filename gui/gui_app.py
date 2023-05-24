import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttkb
from controllers.drives_controller import DrivesController
from controllers.folders_controller import FoldersController
from controllers.files_controller import FilesController
from controllers.context_menu_controller import MenuController
from src.nary_tree import NaryTree
from src.nary_tree_node import NaryTreeNode


class FileExplorer():

    def __init__(self):
        self.tree = NaryTree(NaryTreeNode('C://'))
        self.last_path = {'text': self.tree.root.data}
        self.window = ttkb.Window(themename='darkly')
        self.window.attributes('-fullscreen', True)

        self.window.title('File Explorer')
        self.style = ttk.Style(self.window)
        self.style.configure('Treeview', font=('Bold',13))

        self.user_win_width = self.window.winfo_screenwidth()
        self.left_table_width = int(self.user_win_width * 0.2)
        self.main_table_width = int(self.user_win_width * 0.8)

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
        self.browse_dir = [self.tree.root.data]

        self.context_menu = tk.Menu(self.window, tearoff=False)
        self.context_menu.add_command(label='Rename', command= lambda: self.tree.rename_node(MenuController.route, self.main_table, MenuController.id))
        self.context_menu.add_command(label='Delete', command= lambda: self.tree.remove_node(MenuController.route, self.main_table, MenuController.id))
        self.context_menu.add_command(label='copy', command= lambda: self.tree.copy_and_paste(MenuController.route, self.main_table))
        self.context_menu.add_command(label='Move', command= lambda: self.tree.move(MenuController.route, self.main_table, MenuController.id))
        
        self.top_utils_menu = ttkb.Menu()
        self.down_utils_menu = ttkb.Menu(self.top_utils_menu, tearoff=False)
        self.utils_folder_icon = tk.PhotoImage(file="./assets/folder.png")
        self.utils_file_icon = tk.PhotoImage(file="./assets/file.png")
        self.down_utils_menu.add_command(label="Folder", accelerator="Ctrl+N", command=lambda: FoldersController.create_folder(self.main_table, self.last_path, self.tree), image=self.utils_folder_icon,
                                         compound=tk.LEFT)
        self.down_utils_menu.add_command(label="File", command=lambda: FilesController.create_file(self.last_path, self.tree, self.main_table), image=self.utils_file_icon,
                                         compound=tk.LEFT)
        self.window.bind_all("<Control-n>", lambda: FoldersController.create_folder(self.main_table, self.last_path, self.tree))
        self.down_utils_menu.add_separator()
        self.down_utils_menu.add_command(label="Exit", command=self.window.destroy)
        
        self.top_utils_menu.add_cascade(menu=self.down_utils_menu, label="New")
        
        self.window.config(menu=self.top_utils_menu)

        self.side_table = ttk.Treeview(self.window)

        self.side_table['column'] = ['Drives']
        self.side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        self.side_table.column('Drives', anchor=tk.W,  width=self.left_table_width)
        self.side_table.heading('Drives', text='Drives', anchor=tk.W)

        self.side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.side_table.bind('<<TreeviewSelect>>', lambda e: DrivesController.open_drive(self.last_path, self.side_table, self.main_table, self.tree))

        self.main_table = ttk.Treeview(self.window)

        self.main_table['column'] = ['Files']
        self.main_table.column('#0',  anchor=tk.W, width=0, stretch=tk.NO)
        self.main_table.column('Files', anchor=tk.W, width=self.main_table_width)
        self.main_table.heading('Files', text='File', anchor=tk.W)

        self.main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.main_table.bind('<<TreeviewSelect>>', lambda e: FoldersController.open_folder(self.main_table, self.tree, self.context_menu, self.last_path))
        DrivesController.find_valid_drives(self.drives, self.valid_drives)

        DrivesController.insert_drives(self.side_table, self.valid_drives)

    def run(self):
        self.window.mainloop()