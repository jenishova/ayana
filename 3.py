#3

#Напишите функцию, которая принимает возраст собаки и нужно вычислить, возраст собаки в человеческих годах.
#(В течение первых двух лет собачий год равен 10.5 человеческим годам.
#После этого каждый год собаки равен 4 человеческим годам).



age = 10

def dog_age():

    if age==1 or age==2:
        print(age*10.5)
    elif age > 2:
        print(10.5*2 + (age-2)*4)

dog_age()
