def read_user_number(user_prompt: str, lower_bound: float = 0, upper_bound: float = 9999999):
    """
    Отвечает за считывание у пользователя строки и конвертации её в число
    Считывание происходит до тех пор, пока введённая строка не удовлетворит все условия
    :param user_prompt: комментарий для контекста пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: считанное у пользователя число в рамках допустимых значений
    """
    while True:
        number = input(f'{user_prompt}\n>')
        try:
            number = int(number)  # int так как нам нужны только целые числа
            if lower_bound < number < upper_bound:
                return number
            else:
                print(f'Введите секунды в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def time_converter() -> dict:
    """
    Функция берет значение пользователя и выполняют математическую часть
            :return: Возвращает готовый словарь с нужными значениями
    """
    seconds_remain = sec_input % (24 * 3600)
    days = sec_input // (24 * 3600)
    hours = seconds_remain // 3600
    minutes = sec_input % 3600 // 60
    seconds = sec_input % 60
    time_dict = {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
    return time_dict


if __name__ == '__main__':
    print("Вас приветствует программа по переводу секунд в Дни Часы Минуты Секунды")  # приветствие
    sec_input = read_user_number("Введите ваши секунды-->")  # запрос на ввод от пользователя
    print(time_converter())  # печать готового результата
