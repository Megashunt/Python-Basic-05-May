#  input_msg = input("Введите свой текст:")
#  print(input_msg[::-1])

#  input_name = input("Введи имя: ")
#  answer = f"Hello, {input_name}"
#  print(answer)

word = input('Write your word:')
word = word.lower()
word_2 = word[::-1]
if word == word_2:
    print('Yes')
else:
    print("No")
