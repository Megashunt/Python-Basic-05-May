while True:  # используем для того чтобы программа находилась в цикле
    # запрашиваем ввод пользователя для дальнейшего поиска ключевых слов
    input_1 = input('>').lower().strip()
    greeting_1 = input_1.find("привіт")
    greeting_2 = input_1.find("хай")
    greeting_3 = input_1.find("доброго дня")
    question_1 = input_1.find("як справи")
    question_2 = input_1.find("що робиш")
    question_3 = input_1.find("чим займаєшся")
    movie = input_1.find("фільм")
    cinema = input_1.find("кінотеатр")
    series = input_1.find("серіал")
    goodbye_1 = input_1.find("бувай")
    goodbye_2 = input_1.find("надобраниіч")
    goodbye_3 = input_1.find("гудбай")
    # конструкция if elif для ответа на найденные ключевые слова.
    # логика ниже основана на результате .find если ключевое слово найдено то резудьтат будет >= 0 и последует овтет
    if greeting_1 >= 0 or greeting_2 >= 0 or greeting_3 >= 0:
        print("Доброго вечора, я бот з України!")
    elif question_1 >= 0 or question_2 >= 0 or question_3 >= 0:
        print("Вчусь програмувати на Python!")
    elif movie >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм 'Tenet',""він просто бомба!")
    elif cinema >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але сходить подивіться 'Tenet' у кінотеатри, "
              "він просто бомба!")
    elif series >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал 'Wednesday',"
              "він просто бомба!")
    elif goodbye_1 >= 0 or goodbye_2 >= 0 or goodbye_3 >= 0:
        print("Побачимось у мережі, I'll be back.")
        break  # программа закрывается после прощания пользователя
    else:  # ответ в случае отсутвия ключевого слова
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
# input_1 = input('>').lower().strip()
#
# if "хай" in input_1:
#     print("Доброго вечора, я бот з України!")
# else:
#     print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")