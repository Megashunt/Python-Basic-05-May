input_1 = input("Please, input your string:")  # HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :)
input_1 = input_1.lower()  # Програма переводить строку в нижній регістр
input_1 = input_1.replace('.', '')
input_1 = input_1.replace(',', '')
input_1 = input_1.replace('-', '')
input_1 = input_1.replace(';', '')
input_1 = input_1.replace(':', '')
input_1 = input_1.replace('?', '')
input_1 = input_1.replace('!', '')
# input_1 = input_1.replace(')', '')
# Програма видаляє зі строки такі символи пунктуації: .,-:;?!
input_1 = input_1.rstrip()  # Програма видаляє зайві пробіли\табуляції з правого кінця строки
input_2 = input("What do you want to replace?").lower()  # C++
index_1 = input_1.find(input_2)
print(index_1)
output_1 = print(f'"{input_2.upper()}", was found at position {index_1}')
input_3 = input("With what do you want to replace?")
output_2 = input_1.replace('c++', input_3)
print(output_2)