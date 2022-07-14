
#1

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print(add(2, 4))
print(substract(2, 4))
print(multiply(2, 4))
print(divide(2, 4))

#2

def my_list(argument):
    symbols = 0
    for i in argument:
        symbols += 1
    print(symbols)
    letters = 0
    for i in argument.replace(' ', ''):
        letters += 1
    print(letters)
my_list('hello world')

#3
def my_list(a = {}, b = {}):
    a = list(dict.keys(a)), list(dict.values(a))
    print(a)

my_list({1: 'tata', 2: 'cooky'},{ 3: 'chimmy', 4: 'koya'})

#4
print(input('what are you want eat? '))
def my_list(a, b):
    with open('menu.txt', 'w') as file:
         file.write(a)
         file.write(b)

my_list('ramen', 'potato')

#5

def my_file(str):
    with open(str, 'w') as file:
        file.write('')

my_file('tata')


#6
def function_1():
    print("Я главная функция")
    def function_2():
        print("Я вложенная функция.")
    function_2()
function_1()

#7

def my_list(a = {}):   
    a = list(dict.keys(a)), list(dict.values(a))
    print(a)
my_list({1: 'tata', 2: 'cooky', 3: 'chimmy', 4: 'koya'})


#8

def my_list(a):
    if a % 2 == 0:
        return a == 2
    b = 6
    while b * b <= a and a % b != 0:
        b += 2
    return b * b > a

print(my_list(int(input("Enter a number: "))))



