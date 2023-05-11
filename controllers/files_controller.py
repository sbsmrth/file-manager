import os

def insert_files(table, path, browse_dir):
    for i in table.get_children():
        table.delete(i)

    files = os.listdir(path)

    browse_dir = []

    for r in range(len(files)):
        table.insert(parent='', iid=r, text='', index='end', values=[files[r]])
        browse_dir.append(f"{str(path)}/{files[r]}")