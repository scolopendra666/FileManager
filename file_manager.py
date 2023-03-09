import os
import shutil
import datetime


class FileManager:
    def __init__(self):
        self.storage_directory = "file_storage"
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)

    def save_file(self, file_path):
        file_id = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(self.storage_directory, file_id + '.' + file_path.split('.')[-1])
        shutil.copy(file_path, destination_path)
        return file_id

    def get_file_path(self, file_id):
        file_path = os.path.join(self.storage_directory, file_id)
        if os.path.exists(file_path):
            return file_path
        return None

    def delete_file(self, file_id):
        path_to_directory = os.path.abspath("file_storage")
        for filename in os.listdir(path_to_directory):
            if filename.startswith(file_id):
                os.remove(os.path.join(path_to_directory, filename))

    def rename_file(self, old_file_id, new_file_id):
        old_file_path = self.get_file_path(old_file_id)
        new_file_path = os.path.join(self.storage_directory, new_file_id)
        if old_file_path and not os.path.exists(new_file_path):
            os.rename(old_file_path, new_file_path)

    def get_file_paths(self, file_ids):
        file_paths = []
        for file_id in file_ids:
            file_path = self.get_file_path(file_id)
            if file_path:
                file_paths.append(file_path)
        return file_paths

    def list_file(self):
        files = []
        for file_id in os.listdir(self.storage_directory):
            file_path = self.get_file_path(file_id)
            if file_path:
                files.append([file_id, os.path.abspath(file_path)])
        return files

    def get_file_path_by_id(self, id):
        path_to_directory = os.path.join(os.getcwd(), "file_storage")
        for filename in os.listdir(path_to_directory):
            if filename.startswith(id):
                path_to_file = os.path.join(path_to_directory, filename)
                return path_to_file
                



