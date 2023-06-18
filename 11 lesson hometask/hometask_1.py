def add_note() -> str:
    """
    Функция для запроса заметки у пользователя
    :return: Строку которую ввели
    """
    note_input = input("Введите заметку:")
    return note_input


def how_many_display(lower_bound: int = 0, upper_bound: int = 99) -> int:
    """
    Узнаем у пользователя сколько заметок отобразить
    :return:
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
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def earliest_note():
    """
    Функция по запросу пользователя выдает нужное количество отсортированных заметок. Т.к. список сохраняет по порядку
    :return:отсутствует т.к. вывод происходит внутри функции
    """
    number_1 = how_many_display()
    notes_keeper_f.seek(0)
    notes_list_1 = notes_keeper_f.read().splitlines()
    earliest_notes_list = notes_list_1[:number_1]
    print("От ранней к поздней:", *earliest_notes_list, sep="\n")


def latest_note():
    """
    Функция по запросу пользователя выдает нужное количество отсортированных заметок. Сначала отзеркаливает список
    потом выдает нужное количество заметок
    :return:отсутствует т.к. вывод происходит внутри функции
    """
    number_2 = how_many_display()
    notes_keeper_f.seek(0)
    notes_list_2 = notes_keeper_f.read().splitlines()
    latest_notes_list = notes_list_2[::-1]
    print("От поздней к ранней:", *latest_notes_list[:number_2], sep="\n")


def shortest_note():
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок. Из заготовленных списков
        делается словарь, затем словарь перебирается в новый список с сортировкой по значению длинны. Вывод результата
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    notes_keeper_f.seek(0)
    len_notes_keeper_f.seek(0)
    notes_list_3 = notes_keeper_f.read().splitlines()
    len_of_notes_list = len_notes_keeper_f.read().splitlines()
    dict_with_notes = dict(zip(notes_list_3, len_of_notes_list))  # собираем словарь из двух списков
    #  TODO сортировку с lambda
    # способ с урока sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()])  # делаем список отсортированный по значениям
    number_3 = how_many_display()
    print("Від найкоротшої до найдовшої:")
    flag_1 = 0  # флаг для цикла
    for i in tmp_sorted_list:  # перебираем список печатая только каждый второй элемента из списка в списке)
        print(i[1])
        flag_1 += 1
        if flag_1 == number_3:
            break


def longest_note():
    """
        Функция по запросу пользователя выдает нужное количество отсортированных заметок
        :return:отсутствует т.к. вывод происходит внутри функции
        """
    notes_keeper_f.seek(0)
    len_notes_keeper_f.seek(0)
    notes_list_4 = notes_keeper_f.read().splitlines()
    len_of_notes_list = len_notes_keeper_f.read().splitlines()
    dict_with_notes = dict(zip(notes_list_4, len_of_notes_list))  # собираем словарь из двух списков
    #  TODO сортировку с lambda
    # способ с урока sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()], reverse=True)
    number_4 = how_many_display()
    flag_2 = 0
    print("Від найдовшої до найкоротшоЇ:")
    for i in tmp_sorted_list:  # цикл для вывода только второго значения из списка в списке
        print(i[1])
        flag_2 += 1
        if flag_2 == number_4:  # цикл работает пока флаг не совпадет со значением которое дал пользователь
            break


if __name__ == "__main__":
    print("Добро пожаловать в заметки. Введите ваши заметки по очереди. Используйте 'add' чтобы добавить заметку, \n"
          "'earliest' для отображения в хронологическом порядке, 'latest' для отображения в обратном хронологическом \n"
          "порядке, 'longest' для отображения в порядке увеличения длинны, 'shortest'  для отображения в порядке \n"
          "уменьшения длинны, 'save or exit' для сохранения и выхода ")
    with open('notes_keeper.txt', mode='a+', encoding='utf-8') as notes_keeper_f:
        with open('len_notes_keeper.txt', mode='a+', encoding='utf-8') as len_notes_keeper_f:
            while True:
                user_input = input('->')
                key_word = user_input.lower().split()
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
                elif 'quit' or 'exit' in key_word:  # доп функция для доп балов :))
                    break
