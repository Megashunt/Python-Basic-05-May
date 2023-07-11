from uuid import uuid4
import csv
import os


class CSVProcessor:
    def __init__(self, path):
        self.path = path
        self.filepaths = [f for f in os.listdir(path) if f.endswith('.csv')]

    def all_csv_data_list(self):
        for each_path in self.filepaths:
            global_file_paths = self.path + each_path
            with open(global_file_paths, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                rows = list(reader)
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



if __name__ == '__main__':
    x = CSVProcessor(r'/Users/advakhov/Рабочая папка /PyCharm/final_hometask  /SKU/')
    print(CSVProcessor.all_csv_data_list(x))
