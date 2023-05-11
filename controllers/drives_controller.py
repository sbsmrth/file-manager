import os
from folders_controller import insert_folders

def insert_drives(table, valid_drives):

    for i in table.get_children():
        table.delete(i)

    for r in range(len(valid_drives)):
        table.insert(parent='', iid=r, text='', values = [valid_drives[r]], 
                     index='end')

def find_valid_drives(drives, valid_drives):
    
    for drive in drives:
        if os.path.exists(drive):
            valid_drives.append(drive)

    # insert_drives(valid_drives)

def open_drive(table, main_table, valid_drives, browse_dir):
    index = int(table.selection()[0])
    path = valid_drives[index]

    insert_folders(path, main_table, browse_dir)