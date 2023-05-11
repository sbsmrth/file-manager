import tkinter as tk
import tkinter.ttk as ttk
from controllers import drives_controller


window = tk.Tk()
window.geometry('600x600')
#icono
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

#metodo  def insert_drives()

#metodo def find_valid_drives ()

#metodo def insert_folders(path)

#metodo def open_drive()

#metodo def insert_files

#metodo def open_folder

side_table = ttk.Treeview(window)

side_table['column'] = ['Drives']
side_table.column('#0', anchor=tk.W, width=0, stretch=tk.NO)
side_table.column('Drives', anchor=tk.W,  width=120)
side_table.heading('Drives', text='Drives', anchor=tk.W)


side_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
#side_table.bind('<<TreeviewSelect>>' lambda e:open_drive())
side_table.bind('<<TreeviewSelect>>', lambda e: drives_controller.open_drive())

main_table = ttk.Treeview(window)

main_table['column'] = ['Files']
main_table.column('#0',  anchor=tk.W, width=0, stretch=tk.NO)
main_table.column('Files', anchor=tk.W, width=500)
main_table.heading('Files', text='File', anchor=tk.W)

main_table.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
#main_table.bind('<<TreeviewSelect>>', lambda e:open_folder() )
main_table.bind('<<TreeviewSelect>>', )
#llamada del metodo find_valid_drives ()

window.mainloop()