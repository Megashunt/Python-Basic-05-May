import os
KEY_WORDS = ['add', 'earliest', 'latest', 'shortest', 'longest', 'quit', 'exit', 'save']


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


def add_note() -> str:
    """
    Функция для запроса заметки у пользователя
    :return: Строку которую ввели
    """
    note_input = input("Введите заметку:")
    return note_input


def how_many_display(lower_bound: int = 0, upper_bound: int = 99) -> int:
    """
    Узнаем сколько вывести заметок
    :param lower_bound: Нижний предел
    :param upper_bound: Верхний предел
    :return: Целое число
    """
    while True:
        number = input("Сколько заметок вывести на экран?->")
        try:  # для устойчивости кода к некорректному вводу
            number = int(number)
            if lower_bound < number < upper_bound:
                return number
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить целое число из ввода: "{number}", повторите пожалуйста попытку')


def earliest_note():
    """
    Функция по запросу пользователя выдает нужное количество отсортированных заметок.
    :return:отсутствует т.к. вывод происходит внутри функции
    """
    number_1 = how_many_display()
    notes_keeper_f.seek(0)
    notes_list_1 = notes_keeper_f.read().splitlines()
    earliest_notes_list = notes_list_1[:number_1]
    print("От ранней к поздней:", *earliest_notes_list, sep="\n")


def latest_note():
    """
    Функция по запросу пользователя выдает нужное количество отсортированных заметок.
    :return:отсутствует т.к. вывод происходит внутри функции
    """
    number_2 = how_many_display()
    notes_keeper_f.seek(0)
    notes_list_2 = notes_keeper_f.read().splitlines()
    latest_notes_list = notes_list_2[::-1]
    print("От поздней к ранней:", *latest_notes_list[:number_2], sep="\n")


def dict_notes_with_len(notes_wrapper, len_notes_wrapper) -> dict:
    """
    Соединяет два текстовых файла из заметок и длинны этих заметок для корректной сортировки
    :param notes_wrapper:  принимаем текст записок
    :param len_notes_wrapper: принимаем текст длинны записок
    :return: готовый словарь - текст записки: длинна
    """
    notes_wrapper.seek(0)
    len_notes_wrapper.seek(0)
    notes_list_3 = notes_wrapper.read().splitlines()
    len_of_notes_list = len_notes_wrapper.read().splitlines()
    dict_with_notes = dict(zip(notes_list_3, len_of_notes_list))
    return dict_with_notes


def shortest_note():
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок. Из заготовленных списков
        делается словарь, затем словарь перебирается в новый список с сортировкой по значению длинны. Вывод результата
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    shortest_dict = dict_notes_with_len(notes_wrapper=notes_keeper_f, len_notes_wrapper=len_notes_keeper_f)
    tmp_sorted_list = sorted([(v, k) for k, v in shortest_dict.items()])
    number_3 = how_many_display()
    print("Від найкоротшої до найдовшої:")
    flag_1 = 0  # флаг для цикла
    for i in tmp_sorted_list:
        print(i[1])
        flag_1 += 1
        if flag_1 == number_3:
            break


def longest_note():
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    longest_dict = dict_notes_with_len(notes_wrapper=notes_keeper_f, len_notes_wrapper=len_notes_keeper_f)
    tmp_sorted_list = sorted([(v, k) for k, v in longest_dict.items()], reverse=True)
    number_4 = how_many_display()
    print("Від найдовшої до найкоротшої:")
    flag_1 = 0  # флаг для цикла
    for i in tmp_sorted_list:
        print(i[1])
        flag_1 += 1
        if flag_1 == number_4:
            break


if __name__ == "__main__":
    print("Добро пожаловать в заметки. Используйте 'add' чтобы добавить заметку, \n"
          "'earliest' для отображения в хронологическом порядке, 'latest' для отображения в обратном хронологическом \n"
          "порядке, 'longest' для отображения в порядке увеличения длинны, 'shortest'  для отображения в порядке \n"
          "уменьшения длинны, 'save or exit' для сохранения и выхода ")
    #  для доп баллов реализованна возможность выбора файла с которым работать
    file_name = str(input('Какой файл открыть?')).lower().strip()
    if os.path.isfile(file_name):
        print(f'Чтение файла {file_name}...')
        notes_keeper_f = open(file_name, mode='a+', encoding='utf-8')
        len_notes_keeper_f = open(f'{file_name}_len_notes_keeper.txt', mode='a+', encoding='utf-8')
    else:
        print(f'Такого файла нет: {file_name}, создаём файл...')
        notes_keeper_f = open(file_name, mode='a+', encoding='utf-8')
        len_notes_keeper_f = open(f'{file_name}_len_notes_keeper.txt', mode='a+', encoding='utf-8')
    #  цикл который работает с ключевыми словами
    while True:
        key_word = key_word_input()
        if 'add' in key_word:
            user_note = add_note()
            len_user_note = str(len(user_note))
            notes_keeper_f.write(user_note + '\n')
            len_notes_keeper_f.write(len_user_note + '\n')
        elif 'earliest' in key_word:
            earliest_note()
        elif 'latest' in key_word:
            latest_note()
        elif 'shortest' in key_word:
            shortest_note()
        elif 'longest' in key_word:
            longest_note()
        elif 'quit' or 'exit' or 'save' in key_word:  # save & exit
            print("Пока кожаный мешок, сохранение... закрытие...")
            notes_keeper_f.close()
            len_notes_keeper_f.close()
            break
