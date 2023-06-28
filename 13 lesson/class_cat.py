from random import choices, randint, random


class Cat:
    def __init__(self, name: str, age: int, preferred_food: set):
        """
        класс кошка
        :param name: принимаем в класс Имя
        :param age: возраст
        :param preferred_food: и предпочитаемая еда
        """
        #  аттрибуты класса
        self.name = name
        self.age = age
        self.preferred_food = preferred_food
        self.hungry = 0
        self.hours_outdoors = 0

    def __str__(self):
        """
        Для красивого отображения функции при запросе вывода используем эту конструкцию
        :return: в терминал выйдет то что тут возвращаем
        """
        starting_str = f"Кошка {self.name}, {self.age} "
        if self.age == 1:
            starting_str += "год"
        elif 2 <= self.age <= 4:
            starting_str += "года"
        else:
            starting_str += "лет"
        hungry_status = 'Не голоден' if self.hungry > 0 else 'Голоден'
        starting_str += f", часов гулял: {self.hours_outdoors}, {hungry_status}"
        return starting_str

    def meow(self, count: int):
        if count > 0:
            meow_str = '-'.join(["Мяу"] * count).capitalize()
            print(f"{self.name} мяукает: {meow_str}!")

    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} кушает {food}")
                self.hungry += 1
            else:
                print(f"{self.name} такое не ест: {food}")
                self.meow(randint(1, 5))
        else:
            print(f"{self.name} не голоден")

    def walk(self, alone: bool):
        """
        Собака гуляет
        :param alone: если True, то собака гуляет одна, если False - то с хозяином
        Если собака гуляла суммарно больше 3 часов, то она проголодалась
        :return: если с хозяином - повышается настроение (у хозяина), если сама - None
        """
        if alone:
            hours = randint(2, 4)
            with_str = "сам"
        else:
            hours = randint(1, 3)
            with_str = "с хозяином"
        print(f"{self.name} гуляет {with_str} {hours} часов")
        self.hours_outdoors += hours
        if self.hours_outdoors > 3:
            self.hungry -= 1
        return "Настроение улучшилось!" if not alone else "Настроение без изменений("
