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
    x = CSVProcessor(r'/final_hometask/core/SKU/')
    print(CSVProcessor.all_csv_data_list(x))

  new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            x = data_entry[column_name]
            y = datetime.datetime.strptime(x, '%d-%b-%Y')
            new_index[y] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index

new_index = dict()
for data_entry in all_data:
    if data_entry[column_name] not in new_index:
        new_index[data_entry[column_name]] = list()

    new_index[data_entry[column_name]].append(data_entry)
return new_index

from csvprocessor import CSVProcessor
import datetime


def create_index(all_data: list, column_name: str) -> dict:
    """
    Для индексирования даты из списка в словарь по нужной колонке
    :param all_data: файл
    :param column_name: название колонки для индексации
    :return: Словарь в формате название колонки:[data]
    """
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()

        new_index[data_entry[column_name]].append(data_entry)
    return new_index

def exp_create_index(all_data: list, column_name: str) -> dict:
    """
    Для индексирования даты из списка в словарь по нужной колонке
    :param all_data: файл
    :param column_name: название колонки для индексации
    :return: Словарь в формате название колонки:[data]
    """
    new_index = dict()
    for data_entry in all_data:
        x = data_entry[column_name]
        y = datetime.datetime.strptime(x, '%d-%b-%Y')
        if data_entry[column_name] not in new_index:
            new_index[y] = list()
        new_index[y].append(data_entry)
    return new_index

def quantity_and_statistic(all_data: dict, key_index: str, quantity=True):
    """
    Согласно запросу пользователя выдает информацию или статистику по определенному бренду или категории
    :param all_data: словарь из unique_id_func()
    :param key_index: запрос пользователя
    :param quantity: переключатель
    :return: отсутствует
    """
    list_1 = list()
    list_2 = list()
    for key1_2, value1_2 in all_data.items():
        # Проход по внутренним ключам
        for key2_2, value2 in value1_2.items():
            if value2 == key_index:
                list_1.append(key1_2)
                list_2.append(float(all_data[key1_2]['operation_cost']))
    print(sum(list_2))
    return list_1


def statistic_for_brand_and_cat(all_data: dict, key_index_1: str):
    """
    Hахує розподіл товарів по брендам для кожної категорії та виводить це на екран
    :param all_data: словарь из unique_id_func()
    :param key_index_1: название колонки
    :return: отсутствует
    """
    list_1 = list()
    for key1_2, value1_2 in all_data.items():
        # Проход по внутренним ключам
        for key2_2, value2 in value1_2.items():
            if value2 == key_index_1:
                list_1.append(all_data[key1_2]['brand'])
    result = {i: list_1.count(i) for i in list_1}
    print(result)


if __name__ == '__main__':
    process_directory = CSVProcessor(r'/Users/advakhov/Рабочая папка /PyCharm/final_hometask/SKU/')
    csv_data_list = CSVProcessor.all_csv_data_list(process_directory)
    csv_data_dict = CSVProcessor.all_csv_data_dict_unique(process_directory)
    # # indx
    # indx_sku = create_index(csv_data_list, "sku")
    # print(indx_sku)
    # indx_wrhs = create_index(csv_data_list, "warehouse")
    # print(indx_wrhs)
    # indx_oprtn = create_index(csv_data_list, "operation")
    # print(indx_oprtn)

    # # metrics
    # sale_sum = quantity_and_statistic(csv_data_dict, "sale")

    # exp_date_indx
    # exp_date_sku = exp_create_index(csv_data_list, "expiration_date")
    # print(exp_date_sku)


