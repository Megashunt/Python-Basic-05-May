from math import sqrt  # импорт для квадратного корня


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
                return number
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except (ValueError, TypeError):
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')


def triangle_check() -> bool:
    """
    Функция для определения возможности существования треугольника с булевым возвратом результата
    :return: True если существует False если нет
    """
    if a + b > c and a + c > b and b + c > a:
        return True


def triangle_perimeter() -> float:
    """
    Функция для подсчета периметра
    :return: значение периметра
    """
    perimeter = a + b + c
    return perimeter


def triangle_square() -> float:
    """
    Функция для нахождения площади треугольника
    :return: готовое значение площади
    """
    half_p = (a + b + c) / 2
    square = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
    return square


if __name__ == '__main__':  # обязательная вставка для разделения основного кода и функций
    print("Вас приветствует программа по определению возможности существования треугольников")  # Приветствующая фраза
    # Переменные которые получают значения из функции
    a = read_user_number("Введите значение первой стороны треугольника-->")
    b = read_user_number("Введите значение второй стороны треугольника-->")
    c = read_user_number("Введите значение третьей стороны треугольника-->")
    if triangle_check() is True:  # в зависимости от булевого значения функции идем по инструкции if или else
        print("Треугольник существует")
        print(f"Периметр треугольника равен {triangle_perimeter()}")
        print(f"Площадь треугольника равна {triangle_square():.2f}")
    else:
        print("Треугольник не существует")
