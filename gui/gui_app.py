import tkinter as tk
import tkinter.ttk as ttk
from controllers.drives_controller import DrivesController
from controllers.folders_controller import FoldersController

class FileExplorer():

    def __init__(self) :
        self.window = tk.Tk()
        self.window.geometry('600x600')

        self.window.title('File Explorer')

        self.style = ttk.Style(self.window)
        self.style.configure('Treeview', font=('Bold',13))

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

        self.side_table = ttk.Treeview(self.window)

        self.side_table['column'] = ['Drives']
        self.side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
        self.side_table.column('Drives', anchor=tk.W,  width=120)
        self.side_table.heading('Drives', text='Drives', anchor=tk.W)

        self.side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.side_table.bind('<<TreeviewSelect>>', lambda e: DrivesController.open_drive(self.window, self.side_table, self.main_table, self.valid_drives, self.browse_dir))

        self.main_table = ttk.Treeview(self.window)

        self.main_table['column'] = ['Files']
        self.main_table.column('#0',  anchor=tk.W, width=0, stretch=tk.NO)
        self.main_table.column('Files', anchor=tk.W, width=500)
        self.main_table.heading('Files', text='File', anchor=tk.W)

        self.main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
        self.main_table.bind('<<TreeviewSelect>>', lambda e: FoldersController.open_folder(self.window, self.main_table, self.browse_dir) )
        DrivesController.find_valid_drives(self.drives, self.valid_drives)

        DrivesController.insert_drives(self.side_table, self.valid_drives)

    def run(self):
        self.window.mainloop()