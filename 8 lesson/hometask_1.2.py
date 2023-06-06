# constant из простых чисел до 100
PRIME_SET = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}


def read_user_number(user_prompt: str, lower_bound: float = 0, upper_bound: float = 101):
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


def prime_number_check() -> bool:
    """
    Проверяет наличие ввода пользователя в сете
    :return: булевое значение true сели есть в сете
    """
    if prime_number_input in PRIME_SET:
        return True
    else:
        return False


if __name__ == '__main__':
    prime_number_input = int(read_user_number("Введите ваше простое число-->"))  # запрос на ввод от пользователя
    print("Это простое число" if prime_number_check() is True else "Это не простое число")
