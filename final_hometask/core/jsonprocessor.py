from .fileprocessor import FileProcessor
import json
import os


class JSONProcessor(FileProcessor):
    """
      Класс наследник FileProcessor. Ищет все файлы с расширением JSON и собирает все данные в один список
      """
    def __init__(self, path: str):
        super().__init__(path=path)
        self.filepaths = [f for f in os.listdir(path) if f.endswith('.json')]

    def all_data_list(self):
        json_data = dict()
        for each_path in self.filepaths:
            global_file_paths = self.path + each_path
            json_data = json.load(open(global_file_paths))
        json_data_list = list()
        for v in json_data.values():
            json_data_list += v
        return json_data_list
