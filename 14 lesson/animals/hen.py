from .animal import Animal
from random import randint


class Hen(Animal):
    """
    Ответственность класса может быть как под именем класса, так и в __init__
    Класс отвечает за симуляцию животного курица
    """
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Кудах-кудах'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'зерно', 'пшено'}
        )
        self.animal_type = 'Курица'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за курицей должное количество времени, мы получаем 10 яиц
        Если меньше - от 1 до 5 яиц
        :param hours: сколько часов ухаживаем
        :return: от 1 до 10 яиц
        """
        if hours > 2:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете десяток куриных яиц')
            return 'Куриных яиц: 10 шт.'
        print(f'Вы ухаживаете за {self} {hours} часов и получаете немного куриных яиц')
        return f'Куриных яиц: {randint(1, 5)}'
