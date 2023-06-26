import csv


def add_column_with_index(old_file, new_file):
    """
    К файлу который дан добавляем колонку с порядковыми номерами. В рамках этой задачи порядковый номер и есть
    уникальный айди
    :param old_file: input file
    :param new_file: output file
    :return: ничего
    """
    with open(old_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Сохраняем заголовок CSV-файла
        rows_with_index = [[str(i + 1)] + row for i, row in enumerate(reader)]  # Добавляем индексы

    with open(new_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Unique_ID'] + header)  # Записываем заголовок с добавленным столбцом "Index"
        writer.writerows(rows_with_index)


def unique_id_func(file_1_csv) -> dict:
    """
    Создает словарь где ключ это уникальный айди а значение это вложенный словарь с данными о товаре"
    :param file_1_csv: файл с уникальными айди
    :return: словарь {уникальный айди: {дата}}
    """
    # как эту функцию надо было сделать по задумке автора?
    with open(file_1_csv, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        my_dict = {}

        for row in csv_reader:
            key_1 = row['Unique_ID']  # Подскажите почему подчеркивает?  Это плохо?
            inner_dict = {}
            # Итерируем по каждому столбцу кроме ключа
            for column in csv_reader.fieldnames[1:]:
                value_1 = row[column]
                inner_dict[column] = value_1

            # Добавляем внутренний словарь в основной словарь
            my_dict[key_1] = inner_dict
        return my_dict


def open_csv_file_dict(filename) -> list:
    """
    Функция для открытия файла с возвратом списка
    :param filename: файл
    :return:List где каждый элемент это словарь в формате колонка:значение
    """
    with open(filename, newline='',) as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        return rows


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


def quantity_and_statistic(all_data: dict, key_index: str, quantity=True):
    """
    Согласно запросу пользователя выдает информацию или статистику по определенному бренду или категории
    :param all_data: словарь из unique_id_func()
    :param key_index: запрос пользователя
    :param quantity: переключатель
    :return: отсутствует
    """
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


def statistic_for_brand_and_cat(all_data: dict, key_index: str, key_index_2: str):
    """
    Hахує розподіл товарів по брендам для кожної категорії(и бренду) та виводить це на екран
    :param all_data: словарь из unique_id_func()
    :param key_index: название колонки
    :param key_index_2: определенный бренд из колонки
    :return: отсутствует
    """
    list_1 = list()
    for key1_2, value1_2 in all_data.items():
        # Проход по внутренним ключам
        for key2_2, value2 in value1_2.items():
            if value2 == key_index:
                list_1.append(all_data[key1_2][key_index_2])
    result = {i: list_1.count(i) for i in list_1}
    print(result)


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
        elif 'last' in key_word:
            input_2 = input('->')
            input_3 = input('->')
            statistic_for_brand_and_cat(id_index, input_2, input_3)

