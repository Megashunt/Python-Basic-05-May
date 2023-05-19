# raw_string = "File disc C:\\"
# print(raw_string)raw_string

# print("90" in "12345")
# str = "a1b2c3d4"
# print(str[0:6:2])

# s = "2"
# print(s.isdigit())

# st_1 = "Hello"
# for letter in st_1:
    # print(letter)

# s = 'pYtHoN'
# print(s.capitalize())

# s = 'IDE provides a toolset for software engineer'
# print(s.title())

# s = '5'
# print(s.isdigit())

# s = '8.0'
# print(s.isdigit())

# s = '4'
# print(type(s))

# s = 'Java programmer'
# print(s.find('Python'))

# s = 'Java programmer'
# print(s.replace('Java', 'Python'))

# s = 'В нас було 5 ноутбуків, 2 сервера та 25 непротестованих прототипів'
# print(s.replace('5', '7'))

# s = 'In Python, numeric types are float and int'
# # довжина строки - 42 символи
# # перший символ має індекс 0, останній - 41
# print(s.find('n'))

# s = 'In Python, numeric types are float and int'
# # довжина строки - 42 символи
# # перший символ має індекс 0, останній - 41
# print(s.rfind('n'))

# s = '25)))))'
# print(s.strip(')'))

import string
print(string.punctuation)
str_1 = "a /:;<=>?@[\]^_`{|}==~'"
print(str_1.strip(string.punctuation))