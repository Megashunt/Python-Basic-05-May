input_1 = input("Please, input your string:").lower()  # HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)
input_1 = input_1.lower()  # Програма переводить строку в нижній регістр
input_1 = input_1.replace('.', '')
input_1 = input_1.replace(',', '')
input_1 = input_1.replace('-', '')
input_1 = input_1.replace(';', '')
input_1 = input_1.replace(':', '')
input_1 = input_1.replace('?', '')
input_1 = input_1.replace('!', '')  # Програма видаляє зі строки такі символи пунктуації: .,-:;?!
# input_1 = input_1.replace(')', '')  # Можно еще и скобоччку удалить
input_1 = input_1.rstrip()  # Програма видаляє зайві пробіли\табуляції з правого кінця строки
# Програма питає користувача яке слово (або словосполучення) він бажає замінити
input_2 = input("What do you want to replace?").lower()  # C++
index_1 = input_1.find(input_2)
# Програма повідомляє на якому індексі строки словосполучення присутнє
print(f'"{input_2.capitalize()}", was found at position {index_1}!')
# Програма питає на яке слово треба замінити
input_3 = input("With what do you want to replace?")
output_2 = input_1.replace(input_2, input_3)
print(output_2)
