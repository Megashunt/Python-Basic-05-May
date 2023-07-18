from .fileprocessor import FileProcessor
from uuid import uuid4
import csv
import os


class CSVProcessor(FileProcessor):
    def __init__(self, path: str):
        super().__init__(path=path)
        self.filepaths = [f for f in os.listdir(path) if f.endswith('.csv')]

    def all_csv_data_list(self):
        for each_path in self.filepaths:
            global_file_paths = self.path + each_path
            with open(global_file_paths, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
                # print(rows)
        return rows

    def all_csv_data_dict_unique(self):
        unique_uuid_index = dict()
        for each_path in self.filepaths:
            global_file_paths = self.path + each_path
            with open(global_file_paths, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
            data_csv = rows
            for _id, row in enumerate(data_csv):
                unique_uuid_index[uuid4()] = row
        return unique_uuid_index
