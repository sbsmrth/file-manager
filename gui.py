import tkinter as tk
import tkinter.ttk as ttk
from controllers.drives_controller import *
from controllers.folders_controller import *

window = tk.Tk()
window.geometry('600x600')

window.title('File Explorer')

style = ttk.Style(window)
style.configure('Treeview', font=('Bold',13))

drives = ['A://', 'B://', 'C://',
          'D://', 'E://', 'F://',
          'G://', 'H://', 'I://',
          'J://', 'K://', 'L://',
          'M://', 'N://', 'O://',
          'P://', 'Q://', 'R://',
          'S://', 'T://', 'U://', 
          'V://', 'W://', 'X://',
          'Y://', 'Z://']

valid_drives = []
browse_dir = []

side_table = ttk.Treeview(window)

side_table['column'] = ['Drives']
side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
side_table.column('Drives', anchor=tk.W,  width=120)
side_table.heading('Drives', text='Drives', anchor=tk.W)

side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
side_table.bind('<<TreeviewSelect>>', lambda e: open_drive(window, side_table, main_table, valid_drives, browse_dir))

main_table = ttk.Treeview(window)

main_table['column'] = ['Files']
main_table.column('#0',  anchor=tk.W, width=0, stretch=tk.NO)
main_table.column('Files', anchor=tk.W, width=500)
main_table.heading('Files', text='File', anchor=tk.W)

main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
main_table.bind('<<TreeviewSelect>>', lambda e: open_folder(window, main_table, browse_dir) )
find_valid_drives(drives, valid_drives)

insert_drives(side_table, valid_drives)

window.mainloop()