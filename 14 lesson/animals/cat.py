from .animal import Animal
from random import randint


class Cat(Animal):
    """
    Ответственность класса может быть как под именем класса, так и в __init__
    Класс отвечает за симуляцию животного курица
    """
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Мур-мур'
    ):
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'каша', 'тортик'}
        )
        self.animal_type = 'Кошка'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за кошкой должное количество времени, мы получаем хорошее настроение
        :param hours: сколько часов ухаживаем
        :return: ничего или хорошее настроение
        """
        if hours > 1:
            print(f'Вы гуляете с {self} {hours} часов и у вас повышается настроение')
            return 'Счастливый Мурчик'
        print(f'Вы гуляете с {self} {hours} часов.')
        return ''
