import os
from .files_controller import FilesController
from .context_menu_controller import MenuController
class FoldersController:

    @staticmethod
    def insert_folders(path, table, browse_dir, menu):
        for item in table.get_children():
            table.delete(item)

        folders = os.listdir(path)

        browse_dir.clear()

        for r in range(len(folders)):
            table.insert(parent='', iid=r, text='', values=[folders[r]], index='end')
            browse_dir.append(f"{str(path)}/{folders[r]}")

        for item in table.get_children():
            table.item(item, tags=item)
            table.tag_bind(item, '<Button-3>', lambda e: MenuController.open(e, menu, table, path))

    @staticmethod
    def open_folder(window, table, browse_dir):
    
        if not table.selection():
            return
        
        index = int(table.selection()[0])

        path = browse_dir[index]

        if os.path.isdir(path):
            FilesController.insert_files(table, path, browse_dir)
        else:
            os.system('"%s"' % path)
        
        window.title(path)