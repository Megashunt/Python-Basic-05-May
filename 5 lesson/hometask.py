my_list = []
while True:
    try:
        input_1 = input('Ваше число:').lower().strip()
        if 'sum' in input_1:
            print(sum(my_list))
            break
        if 'print' in input_1:
            print(my_list)
            continue
        variable_1 = float(input_1)
        my_list.append(variable_1)
    except (ValueError, TypeError):
        print('Введить число или sum, please!')
