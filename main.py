''''''

#Возьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
Code #1:

at = 10
in = 15
wo = 20

for e in range(-at, at):
print(wo / e)
if at > '5':
print("at > 5)
try:
    print("at > 5)
except SyntaxError as se:
    print("ulala")
else:
    print("No exception")
finally:
    print("mimimi")

#3
Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение
Code #2:
list = []
for i in range(10):
list.apend(i)

a = list(revesed(list))
sls_obj = slice('0','8')
print(а[sls_obj])

#4

Перенесите к себе код #3 и исправьте все ошибки, сделайте так чтобы код работал. Если не знаете как исправить ошибку создайте для неё except выражение.
Code #3:
a = (0)
b = (1)
numbers = []
while b > a:
numbers += b
b += 1

