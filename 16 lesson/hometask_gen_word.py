def func_word_gen(words: str):
    words_list = words.split()  # делаем список
    for word in words_list:   # проходим по каждому элементу списика
        yield word


if __name__ == '__main__':
    word_gen = func_word_gen('i am generating words from text')
    while True:  # цикл с инпут для вывода по одному слову
        try:
            input("Нажмите enter тчобы получить следующее слово->")
            print(next(word_gen))
        except StopIteration:  # когда все слова закончатся, программа закроется без ошибки
            break
