#7

#ваша задача — создать функцию, которая превращает строку в мексиканскую волну.
#Вам будет передана строка, и вы должны вернуть эту строку в виде массива, где заглавная буква означает стоящего человека

#Правила:
#1. Строка ввода всегда будет строчной, но может быть и пустой.
#2. Если символ в строке является пробелом, пропустите его, как если бы это было пусто



def mexican_wave(string):
    strings = []

    for idx, char in enumerate(string):
        if char == ' ':
            pass
        else:
            l_string = list(string)
            
            l_string[idx] = l_string[idx].upper()

            l_string = ''.join(l_string)

            strings.append(l_string)
    return(strings)

print(mexican_wave('tata'))


