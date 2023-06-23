import csv


KEY_WORDS = ['index', 'category', 'brand', 'quit', 'exit', 'save']

def add_column_with_index(tech_data, new_tech_data):
    with open(tech_data, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Сохраняем заголовок CSV-файла
        rows_with_index = [[str(i + 1)] + row for i, row in enumerate(reader)]  # Добавляем индексы

    with open(new_tech_data, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Unique_Index'] + header)  # Записываем заголовок с добавленным столбцом "Index"
        writer.writerows(rows_with_index)


def key_word_input() -> str:
    """
    Функция для получения ключевого слово от пользователя.
    :return: Вернет только одно из ключевых слов
    """
    while True:
        key_input = input("Введите ключевое слово->").lower().strip()
        if key_input in KEY_WORDS:
            return key_input
        print(f'Не удалось определить ключевое слово из ввода: "{key_input}", повторите пожалуйста попытку')

def create_index(all_data: list, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список записей из all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


def open_csv_file_dict(filename) -> list:
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        return rows


def create_position_id_index(all_data: list, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем, не дублируя записи
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список порядкового номера записей в all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


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
            print('  ', all_data[i])


if __name__ == '__main__':
    # создаем новый файл с новым столбцом уникальных айди
    # в нашем проекте уникальный айди это порядковый номер из первой колонки
    tech_data = 'tech_inventory.csv'
    new_tech_data_csv = 'new_tech_inventory.csv'
    add_column_with_index(tech_data, new_tech_data_csv)
    new_tech_data = open_csv_file_dict('new_tech_inventory.csv')
    unique_index = create_index(new_tech_data, 'Unique_Index')

    print(unique_index)

    unique_id_index = create_position_id_index(new_tech_data, 'brand')
    print_position_id_index(new_tech_data, unique_id_index)


