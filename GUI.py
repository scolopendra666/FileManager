import os
import tkinter as tk
from tkinter import filedialog

from file_manager import FileManager


class FileManagerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Файловый менеджер")
        self.pack()
        self.file_manager = FileManager()

        self.create_widgets()

    def create_widgets(self):
        # кнопка сохранения файла
        self.save_button = tk.Button(self, text="Сохранить файл", command=self.save_file)
        self.save_button.pack(side="top")


        # кнопка удаления файла
        self.delete_button = tk.Button(self, text="Удалить файл", command=self.delete_file)
        self.delete_button.pack(side="top")

        # кнопка изменения идентификатора файла
        self.rename_button = tk.Button(self, text="Переименовать файл", command=self.rename_file)
        self.rename_button.pack(side="top")

        # кнопка получения списка файлов
        self.list_button = tk.Button(self, text="Список файлов", command=self.list_files)
        self.list_button.pack(side="top")

        # кнопка получения пути одного файла
        self.list_button = tk.Button(self, text="Получение пути файла", command=self.get_path)
        self.list_button.pack(side="top")

        # поле ввода идентификатора файла
        self.id_input = tk.Entry(self, width=70)
        self.id_input.pack(side="top")

        # поле вывода пути до файла
        self.path_output = tk.Label(self, text="")
        self.path_output.pack(side="top")

    def save_file(self):
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Выберите файл для сохранения")
        if filepath:
            file_id = self.file_manager.save_file(filepath)
            self.path_output.config(text="Файл сохранен с идентификатором: {}".format(file_id.split(".")[0]))



    def delete_file(self):
        file_id = self.id_input.get()
        if file_id:
            self.file_manager.delete_file(file_id)
            self.path_output.config(text="Файл с идентификатором {} удален".format(file_id))

    def rename_file(self):
        ids = self.id_input.get()
        new_id, old_id  = ids.split()
        if new_id and old_id:
            self.file_manager.rename_file(old_id, new_id)
            self.path_output.config(text="Файл переименован на {}".format(new_id))

    def list_files(self):
        file_list = self.file_manager.list_file()
        if file_list:
            file_list_str = "\n".join(["id {}: путь {}".format(file_id.split(".")[0], filepath) for file_id, filepath in file_list])
            self.path_output.config(text=file_list_str)
        else:
            self.path_output.config(text="Список файлов пуст")


    def get_path(self):
        file_id = self.id_input.get()
        if file_id
        file_path = self.file_manager.get_file_path_by_id(file_id)
        if file_path:
            self.path_output.config(text=file_path) 
        else:
            self.path_output.config(text="Данного id не существует")


root = tk.Tk()
root.geometry("650x500")
app = FileManagerGUI(master=root)
app.mainloop()
