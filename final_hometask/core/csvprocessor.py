from .fileprocessor import FileProcessor
import csv
import os


class CSVProcessor(FileProcessor):
    """
    Класс наследник FileProcessor. Ищет все файлы с расширением csv и собирает все данные в один список
    """
    def __init__(self, path: str):
        super().__init__(path=path)
        self.filepaths = [f for f in os.listdir(path) if f.endswith('.csv')]

    def all_data_list(self):
        for each_path in self.filepaths:
            global_file_paths = self.path + each_path
            with open(global_file_paths, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
        return rows

