import os

def insert_drives(table, valid_drives):

    for i in table.get_children():
        table.delete(i)

    for r in range(len(valid_drives)):
        table.insert(parent='', iid=r, text='', values = [valid_drives[r]], 
                     index='end')

def find_valid_drives(drives):
    valid_drives = []
    
    for drive in drives:
        if os.path.exists(drive):
            valid_drives.append(drive)

    return valid_drives

    # insert_drives(valid_drives)

def open_drive(table, valid_drives, browse_dir):
    index = int(table.selection()[0])
    path = valid_drives[index]

    insert_folders(path, table, browse_dir)

def insert_folders(path, table, browse_dir):
    for i in table.get_children():
        table.delete(i)

    folders = os.listdir(path)

    browse_dir = []

    for r in range(len(folders)):
        table.insert(parent='', iid=r, text='', values=[folders[r]], index='end')
        browse_dir.append(f"{str(path)}/{folders[r]}")