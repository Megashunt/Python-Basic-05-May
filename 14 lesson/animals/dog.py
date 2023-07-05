from .animal import Animal


class Dog(Animal):
    def __init__(
            self,
            name: str,
            age: int,
            say_word='Гав-гав!'
    ):
        """
        Класс отвечает за симуляцию животного собака
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'каша', 'мясо', 'кость'}
        )
        self.animal_type = 'Собака'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за собакой должное количество времени, мы получаем хорошее настроение
        :param hours: сколько часов ухаживаем
        :return: ничего или хорошее настроение
        """
        if hours > 2:
            print(f'Вы гуляете с {self} {hours} часов и у вас повышается настроение')
            return 'Счастливая Жучка'
        print(f'Вы гуляете с {self} {hours} часов.')
        return ''
