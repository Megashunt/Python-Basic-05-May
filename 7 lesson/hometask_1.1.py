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
            number = float(number)
            if lower_bound < number < upper_bound:
                # return - выход из функции с возвращением некоего значения
                return number
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


if __name__ == '__main__':  # специальный разделитель между функциями и основным кодом
    # Переменные которые получают значения из функции
    fuel_consumption = read_user_number("Введите расход топлива н 100 км-->")
    fuel_price = read_user_number("Введите стоимость топлива за 1л-->")
    distance = read_user_number("Введите дистанцию-->")
    # расчеты и вывод результата
    print("Расход на поездку:", round((fuel_consumption / 100 * distance * fuel_price), 2))
