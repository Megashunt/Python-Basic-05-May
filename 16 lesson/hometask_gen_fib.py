def fib(n: int):  # спасибо stackoverflow
    a, b = 0, 1  # начальные значения для вывовда нуля и единицы
    for fibo in range(n):
        yield a
        a, b = b, a + b  # формула фибоначчи ( принимаем а и б и даем им новые значения)


if __name__ == '__main__':
    user_input = int(input("Сколько чисел фибоначчи вывести? ->"))
    lst = fib(user_input)
    for element in lst:  # для красивого вывода
        print(element)

