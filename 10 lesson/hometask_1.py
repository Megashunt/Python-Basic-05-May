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


if __name__ == "__main__":
    print("Добро пожаловать в заметки. Введите ваши заметки по очереди. Используйте 'add' чтобы добавить заметку, \n"
          "'earliest' для отображения в хронологическом порядке, 'latest' для отображения в обратном хронологическом \n"
          "порядке, 'longest' для отображения в порядке увеличения длинны, 'shortest'  для отображения в порядке \n"
          "уменьшения длинны")
    origin_note_list = list()
    while True:
        user_input = input('->')
        if user_input == 'add':
            origin_note_list.append(add_note())
            print(origin_note_list)  # delete
        elif user_input == 'earliest':
            earliest_note()
        elif user_input == 'latest':
            latest_note()


# my_list = []  # переменная в которую списком будет поступать ввод пользователя
# while True:  # цикл для сбора чисел от пользовтаеля
#     try:
#         input_1 = input('Ваше число или команда:').lower().strip()
#         if 'sum' in input_1:  # проверка на ключевые слова
#             print(sum(my_list))
#             break
#         elif 'clear' in input_1:  # дополнительная фича для дополнительных бaлов
#             my_list.clear()
#             continue
#         elif 'delete' in input_1:  # дополнительная фича для дополнительных бaлов
#             my_list.pop(-1)
#             continue
#         elif 'print' in input_1:  # дополнительная фича для дополнительных бaлов
#             print(my_list)
#             continue  # так как нас интересуют только цифры то без этой комманды дальше будет ошибка
#         variable_1 = float(input_1)
#         my_list.append(variable_1)
#     except (ValueError, TypeError):  # проверку на такие исключения подсмотрел в интеренете
#         print('Введите число или sum, please!')