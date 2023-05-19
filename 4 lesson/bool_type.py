# int()
x = 5
print(x, type(x))

# float()
x = 5.5
print(x, type(x))

x = 3.0
print(x, type(x))

# str()
x = 'This is string in Python'
print(x, type(x))

x = "This is string in Python"
print(x, type(x))

# bool()
# True 1
# False 0
x = True
print(x, type(x))

x = False
print(x, type(x))

x = False

if x:
    print('Условие истинное!')
# иначе
else:
    print('Условие ложное')

if 5 > 3:
    print('5 больше 3')
else:
    print('5 меньше 3')

if 5 < 3:
    print('5 меньше 3')
else:
    print('5 больше 3')

if 5 <= 3:
    print('5 меньше или равно 3')
else:
    print('5 больше или равно 3')

if 5 >= 3:
    print('5 больше или равно 3')
else:
    print('5 меньше или равно 3')

if 5 == 5:
    print('5 равно 5')
else:
    print('5 не равно 5')

if 5 != 3:
    print('5 не равно 3')
else:
    print('5 равно 3')

if 'Python'.lower() == 'python'.lower():
    print('Строки равны в нижнем регистре')

if not False:
    print('Это истинно')

expenses = 100
limit = 80
if not expenses > limit:
    print('Траты не превышают лимит')
else:
    print('Траты превышают лимит')

source = input('Введите строку: ')
search_query = input('Введите подстроку, которую нужно найти: ')
if search_query.lower() in source.lower():
    print(f'Подстрока {search_query} есть в {source}')
else:
    print(f'Подстроки {search_query} нет в {source}')

x = ' '
if x:
    print(f'{x} это правда')
else:
    print(f'{x} это неправда')

# Конструкция ветвления
# если
# if <conditional expression>:
# if <условное выражение>:
#     с отступом (Tab или 4 пробела) пишем тело условие
#       что происходит если условное выражение в if "срабатывает"
# elif <условное выражение>:
#     с отступом пишем тело elif
#       что происходит когда условие в if не срабатывает,
#       а условие в elif - срабатывает
# "много других elif"
# elif <условное выражение>:
#     с отступом пишем тело elif
#       что происходит когда условие в if и предыдущем elif не срабатывает,
#       а условие в этом elif - срабатывает
# else:
#     с отступом пишем тело else
#        что происходит когда условие в if не срабатывает

# Операторы условных выражений
# > >= < <= - больше/меньше/или равно для чисел int float
# == != - равно и неравно для чисел int float и строк str
# not - отрицание, обратное условие
# in - успешность поиска

# условное выражение "конвертируется" в bool.
#   0 или пустая строка - это False.
#   любое другое число или строка - это True