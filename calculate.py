def math():
    while True:
        action = input('Знак: ')
        num1 = int(input('a: '))
        num2 = int(input('b: '))


        if action == '+':
            print(num1, '+', num2, '=', num1 + num2)
        elif action == '-':
            print(num1, '-', num2, '=', num1 - num2)
        elif action == '*':
            print(num1, '*', num2, '=', num1 * num2)
        elif action == '/':
            print(num1, '/', num2, '=', num1 / num2)
        else:
            print('Ошибка. Не тот знак')
            math()


math()