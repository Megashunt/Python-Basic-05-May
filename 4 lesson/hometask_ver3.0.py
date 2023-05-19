goodbye_1 = int(-1)
goodbye_2 = int(-1)
goodbye_3 = int(-1)
while goodbye_1 == -1 and goodbye_2 == -1 and goodbye_3 == -1:
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
    if greeting_1 >= 0 or greeting_2 >= 0 or greeting_3 >= 0:
        print("Доброго вечора, я бот з України!")
    elif question_1 >= 0 or question_2 >= 0 or question_3 >= 0:
        print("Вчусь програмувати на Python!")
    elif movie >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм 'Tenet',"
             "він просто бомба!")
    elif cinema >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але сходить подивіться 'Tenet' у кінотеатри, "
              "він просто бомба!")
    elif series >= 0:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал 'Wednesday',"
              "він просто бомба!")
    elif goodbye_1 >= 0 or goodbye_2 >= 0 or goodbye_3 >= 0:
        print("Побачимось у мережі, I'll be back.")
        break
    else:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")
