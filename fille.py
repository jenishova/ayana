'''

#1


f = open('directories.txt', 'r')
print(f.read(today is monday))
f.close()


#2


print('place')


while True:
  login = input('Login: ')
  password = input('Password: ')



  try:
    if login and password:
        with open('users.txt', 'a') as file:
          file.write(f'''{login}/n

{password}/n''')
        break
    else:
        print('bye bye')
        break
  except Exception as e:
    print('Error', e)
    continue



#3

f = open('python.txt', 'r')
print(f.read('Да, в тексте есть w'))
f.close()

'''  

#4


f = open('python.txt', 'w')
f.write( "Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.
")
f.close()
with open('python.txt', 'r') as f:
    print(f.read())
      

