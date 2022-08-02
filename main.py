# '''
# Parking -> талон
# время прибытия --выполнено--
# свобоные места --выполнено--
# высчитывается оплата (почасовая) стоимость (25 сом за час) --выполнено--
# указывается марка и номер авто (01KG123QWE) --выполнено--
# указывать этажи (количества мест) --выполнено--
#
# Инкапсуляция данных
# Интерфейсы
# Валидация данных
# '''
from datetime import datetime, timedelta
class Parking:
     place_count = 20
     __floor = 4
     __total_price = 0
     __cars_numbers = []
     def __init(self, car_model, car_number, time_for_parking):
         self.validate_car_number(car_number)
         self.__car_model = car_model
         self.__car_number = car_number
         self.__time = time_for_parking
         super().__total_price = 25 * self.__time
         Parking.__place_count -= 1
if car_number not in Parking.__cars_numbers:
     Parking.__cars_numbers.append(car_number)
else:
    raise TypeError('Такая машина уже есть в парковке')

def __del(self):
    Parking.cars_numbers.remove(self.__car_number)
    Parking.__place_count += 1

def __str(self):
         time_str = str(datetime.now())
         date_format_str = '%Y-%m-%d %H:%M:%S.%f'
         given_time = datetime.strptime(time_str, date_format_str)
         return f'========================================\nmodel : {self.__car_model}\nnumber : {self.__car_number}\nplase count : {self.check_place_count()}\ntime now : {time_str}\nto time : {given_time + timedelta(hours=self.__time)}\nprice : {self.__total_price} som'


@staticmethod
def check_place_count():
     return Parking.__place_count

@classmethod
def __validate_car_number(cls, number):
         letters = 'qwertyuiopasdfghjklzxcvbnm'.upper()
         if type(number) != str:
             raise TypeError('Номер машины дб строкой')
         if number.isupper() == False:
             raise TypeError('Введите буквы в верхнем регистре')
         region = {
             '01' : 'Bishkek',
             '02' : 'Osh city',
             '03' : 'Batken',
             '04' : 'Jalal-Abat',
             '05' : 'Naryn',
             '06' : 'Osh region',
             '07' : 'Talas',
             '08' : 'Chui',
             '09' : 'IK'
         }
if number[:2] not in region.keys():
             raise TypeError('Несуществующий регион, впишите от 01-09')
    if 'KG' not in number[2:4]:
             raise TypeError('Неверный формат дб "KG"')
    if number[4:7].isdigit() == False:
             raise TypeError('Неверный формат номера дб целые числа (0-9)')
    if number[-3].isalpha() == False or number[-1] not in letters and number[-2] not in letters and number[-3] not in letters:
             raise TypeError('Неверный формат дб латиница (A-Z)')

     @property
     def number(self):
         return self.__car_number
     @number.setter
     def number(self, value):
         self.__validate_car_number(value)
         self.__car_number = value
#
     @staticmethod
     def quantity_of_cars():
         if len(Parking.__cars_numbers) != 0:
             print(f'Parking has {len(Parking.__cars_numbers)} cars ->',Parking.__cars_numbers)
         else:
             print('Parking is empty')

 bmw = Parking('BMW X5', '01KG123DRT', 2)
del bmw
 # print(bmw) # -> 19 свободных мест
mers = Parking('Mers', '01KG124DRT', 3)
    print(mers)
toyota = Parking('Toyta', '01KG125DRT', 5)
    print(toyota)
Parking.quantity_of_cars()
