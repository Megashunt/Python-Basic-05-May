def add_note() -> str:
    note_input = input("Введите заметку")
    return note_input


def earliest_note(lower_bound: int = 0, upper_bound: int = 9999999):
    while True:
        number = input("Сколько заметок вывести на экран?")
        try:
            number = int(number)  # int так как нам нужны только целые числа
            if lower_bound < number < upper_bound:
                earliest_note_list = sorted(origin_note_list[:number])
                print(earliest_note_list)
                break
            else:
                print(f'Введите секунды в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def latest_note(lower_bound: int = 0, upper_bound: int = 9999999):
    while True:
        number = input("Сколько заметок вывести на экран?")
        try:
            number = int(number)  # int так как нам нужны только целые числа
            if lower_bound < number < upper_bound:
                earliest_note_list = sorted(origin_note_list[:number], reverse=True)
                print(earliest_note_list)
                break
            else:
                print(f'Введите секунды в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def shortest_note(lower_bound: int = 0, upper_bound: int = 9999999):
    dict_with_notes = dict(zip(origin_note_list, len_origin_note_list))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()])
    while True:
        number = input("Сколько заметок вывести на экран?")
        try:
            number = int(number)  # int так как нам нужны только целые числа
            if lower_bound < number < upper_bound:
                flag_1 = 0
                for i in tmp_sorted_list:
                    print(i[1])
                    flag_1 += 1
                    if flag_1 == number:
                        break
                break
            else:
                print(f'Введите секунды в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def longest_note(lower_bound: int = 0, upper_bound: int = 9999999):
    dict_with_notes = dict(zip(origin_note_list, len_origin_note_list))
    tmp_sorted_list = sorted([(v, k) for k, v in dict_with_notes.items()], reverse=True)
    while True:
        number = input("Сколько заметок вывести на экран?")
        try:
            number = int(number)  # int так как нам нужны только целые числа
            if lower_bound < number < upper_bound:
                flag_1 = 0
                for i in tmp_sorted_list:
                    print(i[1])
                    flag_1 += 1
                    if flag_1 == number:
                        break
                break
            else:
                print(f'Введите секунды в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')
if __name__ == "__main__":
    print("Добро пожаловать в заметки. Введите ваши заметки по очереди. Используйте 'add' чтобы добавить заметку, \n"
          "'earliest' для отображения в хронологическом порядке, 'latest' для отображения в обратном хронологическом \n"
          "порядке, 'longest' для отображения в порядке увеличения длинны, 'shortest'  для отображения в порядке \n"
          "уменьшения длинны")
    origin_note_list = list()
    len_origin_note_list = list()
    while True:
        user_input = input('->')
        if user_input == 'add':
            user_note = add_note()
            origin_note_list.append(user_note)
            len_origin_note_list.append(len(user_note))
            print(origin_note_list)  # delete
            print(len_origin_note_list)
        elif user_input == 'earliest':
            earliest_note()
        elif user_input == 'latest':
            latest_note()
        elif user_input == 'shortest':
            shortest_note()
        elif user_input == 'longest':
            longest_note()
        elif user_input == 'quit' or 'exit':
            exit()