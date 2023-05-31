input_1 = input("Введите ваш текст для очистки:")  # ()Я не знав куди йти (втім недивно), ((тому)) пішов.().
new_s = ""  # переменная для сбора текста
bracket_condition = False  # переменная для определения скобочек
i = -1  # итератор
while i != (len(input_1) - 1):  # цикл будет работать до последнего символа в строке (last index=Len(str)-1)
    i += 1  # цикл проверяет каждый символ один за другим начиная с нулевого
    if input_1[i] == "(":  # ловушка для текста в скобочке
        bracket_condition = True
    elif input_1[i] == ")":  # отмена ловушки для текста в скобочке
        bracket_condition = False
    else:
        if not bracket_condition:
            new_s += input_1[i]  # пока переменная bracket_condition == False все символы собираются тут
print(new_s)
