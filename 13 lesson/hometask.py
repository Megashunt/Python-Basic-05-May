from class_cat import *


if __name__ == '__main__':
    first_cat = Cat('Матроскин', 1, {'молоко'})
    second_cat = Cat('Кнопка', 2, {'молоко', 'каша'})
    third_cat = Cat('Ворсинка', 3, {'молоко', 'каша', 'колбаса'})
    fourth_cat = Cat("Соня", 4, {'молоко', 'каша', 'колбаса', 'творог'})
    fifth_cat = Cat("Клеопатра", 5, {'молоко', 'каша', 'колбаса', 'творог', 'рыба'})
    sixth_cat = Cat("Масяня", 6, {'корм'})

    cats = [first_cat, second_cat, third_cat, fourth_cat, fifth_cat, sixth_cat]
    potential_food = ['молоко', 'каша', 'колбаса', 'творог', 'рыба', 'корм']
    keyword = input('Кис-киис кис-киис, ты котик я _____ <-')

    if keyword == 'котик':
        for cat in cats:
            events_for_cat = randint(1, 3)  # для рандомного количества событий
            for _ in range(events_for_cat):
                if random() > 0.5:  # веротяность 50/50
                    print(f'Кормим {cat.name}')
                    for random_food in choices(potential_food, k=3):
                        cat.eat(random_food)
                else:
                    if random() > 0.5:
                        result = cat.walk(alone=True)
                    else:
                        result = cat.walk(alone=False)
                    print(f'После прогулки хозяин понял, что: {result}')
            print(f'Прошел день для: {cat}')
            print('=' * 20)
    else:
        print("Ответ не правильный(( (надо было написать 'котик'")
