# Основные принципы ООП
# Наследование
# Полиморфизм
# Инкапсуляция
# Агрегация (Композицией)

# все классы неявно наследуют object
class ParentClass(object):
    def __init__(self, param1, param2):
        print(f'parent class received these parameters: {param1} {param2}')
        self.name = 'I am Parent Class'
        self.x = 5

    def __str__(self):
        return f'My name: {self.name} my x: {self.x}'

    def example_super_function(self):
        return 'I am super function'


# при наследовании нужно указать в скобочках имя класса, который мы наследуем
# class <ИмяКлассаНаследника>(<ИмяКлассаРодителя>):
#   тело класса наследника
class ChildClass(ParentClass):
    def __init__(self, key_param=3):
        # super() обращается к классу-родителю. Superior - вышестоящий с английского.
        # синонимы терминов: SuperClass (parent/родитель) SubClass (child/наследник)
        super().__init__(2, 3)
        self.name = 'I am Child Class'
        self.y = 2

    def example_function(self, y: int):
        return pow(self.x, y)

    def example_super_function(self):
        x = super().example_super_function()
        return x + 'I am sub function'


# наследник тоже может быть родителем и это формирует иерархию
class SubChildClass(ChildClass):
    pass


# можно наследовать несколько классов, это называется множественное наследование
# это весьма сложная и редкоиспользуемая практика
class MultiChildClass(ChildClass, dict):
    pass

# При вызове любого метода или поля объекта, ищется это поле/метод в классе объекта
# Если найдено - выполняется
# Если не найдено - ищется в его родителе. И так дальше пока не дойдут до самого первого родителя.
# Если не найдено ни у кого - ошибка
# Итого выходит, что у самого "младшего" найдут и выполнят метод/поле, не посмотрев на реализацию в родителях.
# Единстввенный способ отослаться на неё - через ключевое слово super()


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    d = {1: 'one', 2: 'two'}
    print()

    p = ParentClass(5, 6)
    c = ChildClass(key_param=10)

    print(p.name)
    print(p)
    print(c.name, c.y)
    print(c)
    # c.name = 'I am Child Class'
    c.x = 3
    print('Changing child NAME')
    print(p.name)
    print(p)
    print(c.name)
    print(c)


    print(c.example_function(2))
    # print(p.example_function(2)) # родитель не получает доступ к методам и полям наследника


    print(p.example_super_function())
    print(c.example_super_function())