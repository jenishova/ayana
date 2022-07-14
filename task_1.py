'''
#1
list_1 = ['name', 'age', '1', '19']
print('Изменённый Лист: ')
def my_list():
    a = int(len(list_1) / 1)
    list_1.reverse()
    list_2 = list_1[:a]
    list_2.reverse()
    list_3 = list_1[a:]
    list_3.reverse()
    print(list_3 + list_1)

my_list()

#2

def my_list(n):
     a , b, c = 1, 1, 2
     for i in range(n):
         yield a
     a, b, c =c, b, a + b + c
list_my_list = list(my_list(10))
print(list_my_list)
   

#3
def plus(a, b):
    print(a + b)
def minus():
    print(a - b)
def all():
   print(plus())
   print(minus())


#4

file_name = input('name of your file: ')
def name():
    file = open('text.txt', 'w')
    file.write('')
    file.close()
file = name()
print(file)
name()

'''

#5
import random
use_1 = '145790'
number = ['0', '4', '4', '4']
def gen_number():
    for i in range(6):
        number.append(random.choice(use_1))
    print(''.join(number))

gen_number()    






