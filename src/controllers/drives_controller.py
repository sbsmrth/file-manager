import os
from .folders_controller import FoldersController

class DrivesController:
    
    @staticmethod
    def insert_drives(table, valid_drives):

        for i in table.get_children():
            table.delete(i)

        for r in range(len(valid_drives)):
            table.insert(parent='', text='', values = [valid_drives[r]], 
                        index='end')

    @staticmethod
    def find_valid_drives(drives, valid_drives):
    
        for drive in drives:
            if os.path.exists(drive):
                valid_drives.append(drive)

    @staticmethod
    def open_drive(base_path, table, main_table, tree):

        if not table.selection():
            return

        FoldersController.insert_folders(base_path, main_table, tree)
