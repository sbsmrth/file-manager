import os
from files_controller import insert_files

def insert_folders(path, table, browse_dir):
    for i in table.get_children():
        table.delete(i)

    folders = os.listdir(path)

    browse_dir = []

    for r in range(len(folders)):
        table.insert(parent='', iid=r, text='', values=[folders[r]], index='end')
        browse_dir.append(f"{str(path)}/{folders[r]}")

def open_folder(table, browse_dir):
    index = int(table.selection()[0])

    path = browse_dir[index]

    if os.path.isdir(path):
        insert_files(table, path, browse_dir)
    else:
        os.system('"%s"' % path)