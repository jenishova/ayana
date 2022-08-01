
#1
def function_1():
    print("Я главная функция")
    def function_2():
        print("Я вложенная функция.")
    function_2()
function_1()

#2

def my_list(a = {}):   
    a = list(dict.keys(a)), list(dict.values(a))
    print(a)
my_list({1: 'tata', 2: 'cooky', 3: 'chimmy', 4: 'koya'})


#3

def my_list(a):
    if a % 2 == 0:
        return a == 2
    b = 6
    while b * b <= a and a % b != 0:
        b += 2
    return b * b > a

print(my_list(int(input("Enter a number: "))))


#4


from random import randint
import random
def my_list():
    print("random numbers", randint(10,50))
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16' '17', '18', '19', '20', '21', '22', '23', '24']
    print("choose random numbers", random.choice(list))
my_list()


#5

def password(func):
    print(input('login: '))
    print(input('password: '))
    try:
        for i in range(start):
            a = chr(i)
except ValueError:
    print("ValueError for i =", i)
    
my_list()


#6

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



