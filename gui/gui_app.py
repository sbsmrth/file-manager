import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttkb
from controllers.drives_controller import DrivesController
from controllers.folders_controller import FoldersController
from controllers.utils_controller import FilesController
from controllers.context_menu_controller import MenuController

class FileExplorer():

    def __init__(self) :
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
        self.browse_dir = []

        self.context_menu = tk.Menu(self.window, tearoff=False)
        self.context_menu.add_command(label='Rename file', command= lambda: FilesController.rename_file( MenuController.route, self.main_table, MenuController.id))
        self.context_menu.add_command(label='Delete File', command= lambda: FilesController.remove_file( MenuController.route, self.main_table, MenuController.id))

        self.side_table = ttk.Treeview(self.window)

        self.side_table['column'] = ['Drives']
        self.side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        self.side_table.column('Drives', anchor=tk.W,  width=self.left_table_width)
        self.side_table.heading('Drives', text='Drives', anchor=tk.W)

        self.side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.side_table.bind('<<TreeviewSelect>>', lambda e: DrivesController.open_drive(self.window, self.side_table, self.main_table, self.valid_drives, self.browse_dir, self.context_menu))

        self.main_table = ttk.Treeview(self.window)

        self.main_table['column'] = ['Files']
        self.main_table.column('#0',  anchor=tk.W, width=0, stretch=tk.NO)
        self.main_table.column('Files', anchor=tk.W, width=self.main_table_width)
        self.main_table.heading('Files', text='File', anchor=tk.W)

        self.main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.main_table.bind('<<TreeviewSelect>>', lambda e: FoldersController.open_folder(self.window, self.main_table, self.browse_dir) )
        DrivesController.find_valid_drives(self.drives, self.valid_drives)

        DrivesController.insert_drives(self.side_table, self.valid_drives)

    def run(self):
        self.window.mainloop()