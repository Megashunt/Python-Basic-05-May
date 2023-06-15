def add_note() -> str:
    """
    Функция для запроса заметки у пользователя
    :return: Строку которую ввели
    """
    note_input = input("Введите заметку:")
    return note_input


def earliest_note(lower_bound: int = 0, upper_bound: int = 99):
    """
    Функция по запросу пользователя выдает нужное количество отсортированных заметок. Т.к. список сохраняет по порядку
    нам надо просто вывести нужное количество заметок
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return:отсутствует т.к. вывод происходит внутри функции
    """
    while True:  # для доп задания, чтобы выводить определенное пользователем количество заметок
        number_1 = input("Сколько заметок вывести на экран?->")
        try:  # для устойчивости кода к некорректному вводу
            number_1 = int(number_1)
            if lower_bound < number_1 < upper_bound:
                earliest_note_list = origin_note_list[:number_1]  # слайс длы вывода нужного количества заметок
                print("От ранней к поздней:", *earliest_note_list, sep="\n")  # * и sep для красивого вывода спика
                break
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number_1}", повторите пожалуйста попытку')


def latest_note(lower_bound: int = 0, upper_bound: int = 99):
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок. Сначала отзеркаливает список
        потом выдает нужное количество заметок
        :param lower_bound: нижнее допустимое значение
        :param upper_bound: верхнее допустимое значение
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    while True:
        number_2 = input("Сколько заметок вывести на экран?->")
        try:
            number_2 = int(number_2)
            if lower_bound < number_2 < upper_bound:
                latest_note_list = origin_note_list[::-1]
                print("От поздней к ранней:", *latest_note_list[:number_2], sep="\n")
                break
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number_2}", повторите пожалуйста попытку')


def shortest_note(lower_bound: int = 0, upper_bound: int = 99):
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок. Из заготовленных списков
        делается словарь, затем словарь перебирается в новый список с сортировкой по значению длинны. Вывод результата
        :param lower_bound: нижнее допустимое значение
        :param upper_bound: верхнее допустимое значение
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    dict_with_notes = dict(zip(origin_note_list, len_origin_note_list))  # собираем словарь из двух списков
    #  в инете нашел такой способ преобразования словаря в список с сортировкой по значению
    # способ с урока sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()])  # делаем список отсортированный по значениям
    while True:
        number_3 = input("Сколько заметок вывести на экран?->")
        try:
            number_3 = int(number_3)
            if lower_bound < number_3 < upper_bound:
                print("Від найкоротшої до найдовшої:")
                flag_1 = 0  # флаг для цикла
                for i in tmp_sorted_list:  # перебираем список печатая только каждый второй элемента из списка в списке)
                    print(i[1])
                    flag_1 += 1
                    if flag_1 == number_3:
                        break
                break
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number_3}", повторите пожалуйста попытку')


def longest_note(lower_bound: int = 0, upper_bound: int = 99):
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок
        :param lower_bound: нижнее допустимое значение
        :param upper_bound: верхнее допустимое значение
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    dict_with_notes = dict(zip(origin_note_list, len_origin_note_list))  # формируем словарь из двух списков
    #  в инете нашел такой способ преобразования словаря в список с сортировкой по значению
    # способ с урока sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()], reverse=True)
    while True:
        number_4 = input("Сколько заметок вывести на экран?->")
        try:
            number_4 = int(number_4)
            if lower_bound < number_4 < upper_bound:
                flag_1 = 0
                print("Від найдовшої до найкоротшоЇ:")
                for i in tmp_sorted_list:  # цикл для вывода только второго значения из списка в списке
                    print(i[1])
                    flag_1 += 1
                    if flag_1 == number_4:  # цикл работает пока флаг не совпадет с значением которое дал пользователь
                        break
                break
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number_4}", повторите пожалуйста попытку')


if __name__ == "__main__":
    print("Добро пожаловать в заметки. Введите ваши заметки по очереди. Используйте 'add' чтобы добавить заметку, \n"
          "'earliest' для отображения в хронологическом порядке, 'latest' для отображения в обратном хронологическом \n"
          "порядке, 'longest' для отображения в порядке увеличения длинны, 'shortest'  для отображения в порядке \n"
          "уменьшения длинны")
    origin_note_list = list()  # обозначаем список для наполнения и хранения заметок
    len_origin_note_list = list()  # список для наполнения и хранения длинны заметок (нужен для shortest/longest)
    while True:
        user_input = input('->')
        key_word = user_input.lower().split()  # для стійкості до некорректного вводу користувача
        # каждому ключевому слову соответствует своя функция def
        if 'add' in key_word:
            user_note = add_note()
            origin_note_list.append(user_note)
            len_origin_note_list.append(len(user_note))  # два списка собираются одновременно с соответствующей инфой
        elif 'earliest' in key_word:
            earliest_note()
        elif 'latest' in key_word:
            latest_note()
        elif 'shortest' in key_word:
            shortest_note()
        elif 'longest' in key_word:
            longest_note()
        elif 'quit' or 'exit' in key_word:  # доп функция для доп балов :))
            break
