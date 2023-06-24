import csv


def add_column_with_index(old_file, new_file):
    with open(old_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Сохраняем заголовок CSV-файла
        rows_with_index = [[str(i + 1)] + row for i, row in enumerate(reader)]  # Добавляем индексы

    with open(new_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Unique_ID'] + header)  # Записываем заголовок с добавленным столбцом "Index"
        writer.writerows(rows_with_index)


def unique_id_func(file_1_csv) -> dict:

    with open(file_1_csv, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        my_dict = {}

        for row in csv_reader:
            key = row['Unique_ID']
            inner_dict = {}
            # Итерируем по каждому столбцу, кроме ключа
            for column in csv_reader.fieldnames[1:]:
                value = row[column]
                inner_dict[column] = value

            # Добавляем внутренний словарь в основной словарь
            my_dict[key] = inner_dict
        return my_dict


def open_csv_file_dict(filename) -> list:
    with open(filename, newline='',) as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        return rows

def create_index(all_data: list, column_name: str) -> dict:
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


def create_position_id_index(all_data: list, column_name: str) -> dict:
    new_index = dict()

    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index

# def print_by_keyword_in_column(d: dict):
#     list_1 = list()
#     for key1_1, value1_1 in d.items():
#         # Проход по внутренним ключам
#         for key2_1, value2_1 in value1.items():
#             if value2_1 is "brand":
#                 list_1.append(key1_1)
#                 print(key1_1, value1_1)
#     list_2 = list_1
#     for element in list_2:
#         print(element)
#         for data in d[element]:
#             print(data, d[element][data])

def print_position_id_index(all_data: list, position_index: dict):
    """
    В удобном формате выводит на экран содержимое переданного индекса по данным
    :param all_data: данные, по которым построен индекс
    :param position_index: индекс, где значения - списки порядковых номеров
    :return: ничего, функция только выводит на экран
    """
    for index_key, position_values in position_index.items():
        print(f'Записи со значением {index_key}')
        for i in position_values:
            print(all_data[i])


def quantity_and_statistic(all_data: dict, key_index: str, quantity=True):
    list_1 = list()
    for key1_2, value1_2 in all_data.items():
        # Проход по внутренним ключам
        for key2_2, value2 in value1_2.items():
            if value2 == key_index:
                list_1.append(key1_2)
    if quantity:
        print(f"Позиции: {key_index} - {len(list_1)} шт.")
    else:
        for element in list_1:
            print(element)
            for data in all_data[element]:
                print(data, all_data[element][data])


if __name__ == '__main__':
    # создаем новый файл с новым столбцом уникальных айди
    # в нашем проекте уникальный айди это порядковый номер из первой колонки
    tech_data = 'tech_inventory.csv'
    new_tech_data_csv = 'new_tech_inventory.csv'
    add_column_with_index(tech_data, new_tech_data_csv)
    id_index = unique_id_func(new_tech_data_csv)  # для словаря в словаря
    new_tech_data_with_id_list = open_csv_file_dict(new_tech_data_csv)
    while True:
        key_word = input('->')
        if 'id' in key_word:
            for key1, value1 in id_index.items():
                print(key1, ':', value1)
        elif 'cat' in key_word:
            index_1 = create_index(new_tech_data_with_id_list, 'category')
            for key,value in index_1.items():
                print(key, ':', value)
        elif 'brand' in key_word:
            index_1 = create_index(new_tech_data_with_id_list, 'brand')
            for key,value in index_1.items():
                print(key, ':', value)
        elif 'show' in key_word:
            input_1 = input("Ведите определенный бренд или категорию для отображения").title()
            quantity_and_statistic(id_index, input_1, quantity=False)
        elif 'statistic' in key_word:
            input_2 = input('->')
            quantity_and_statistic(id_index, input_2)


        # new_tech_data_with_id_list = open_csv_file_dict(new_tech_data_csv)  # для работы индекс 1
        # index_1 = create_index(new_tech_data_with_id_list, 'brand')
        # print(index_1)
        #
        # test = test_test(new_tech_data_with_id)
        #
        # index_2 = create_position_id_index(new_tech_data_with_id_list, 'brand')
        # print(index_2)

        # index_1 = create_index(new_tech_data, 'brand')
        # print(index_1)
