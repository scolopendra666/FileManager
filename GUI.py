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

        # поле ввода идентификатора файла
        self.id_input = tk.Entry(self, width=70)
        self.id_input.pack(side="top")

        # поле вывода пути до файла
        self.path_output = tk.Label(self, text="")
        self.path_output.pack(side="top")