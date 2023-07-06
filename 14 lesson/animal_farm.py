from animals import Dog, Hen, Cow, Cat
from random import choices, randint

if __name__ == '__main__':
    animals = [
        Dog('Жучка', 3),
        Hen('Коко', 2),
        Cow('Милка', 5),
        Cat('Мурчик', 2)   # добавил кошку в список животных
    ]

    available_food = ['сено', 'трава', "зерно", "пшено", "каша", "мясо", "кость", "тортик"]

    what_we_got = list()
    what_we_lost = list()
    doctor_visit = 0  # для подсчет обращений к ветеринару
    sick_animals = list()   # для сбора в одном месте больных животных
    for animal in animals:
        animal.say()
        animal.health_check(randint(0, 1))  # просто рандом для определения больное животное или нет
        """ то же самое, что и ниже
        for i in range(3):
            food = choice(available_food)
            animal.eat(food)
        """
        for food in choices(available_food, k=3):
            what_we_lost.append(food)
            animal.eat(food)
        if animal.hungry:
            print(f'{animal} голодает! Покормите его.')
        what_we_got.append(animal.treat(randint(0, 5)))
        if animal.healthy:  # конструкция которая в заввисимости от состояния животного лечит его
            print(f'{animal} здоров!')
        else:
            print(f'{animal} не здоров!\nВедем к ветеринару!')
            doctor_visit += 1
            sick_animals.append(animal.name)

        print('=' * 20)

    print(f'Сегодня на ферме мы потратили: {", ".join(what_we_lost)} и\nполучили: {", ".join(what_we_got)}.\n'
          f'Ветеринар посмотрел {doctor_visit} животных, а именно: {", ".join(sick_animals)} ')  # отчет связанный
    # со здоровьем
    