import random
from datetime import datetime

# fruits = ["apple", "cherry", "orange", "kiwi", "melon", "banana",  "mango"]
# random_element = random.randint(0, len(fruits) -1)
# print(fruits[random_element])

# print second element
# print(fruits[1])

# # print list elements from second to four

# print(fruits[1:5])

#  sort list and then replace cherry with lemon
# second approach With map and lambda function
# fruits.sort()
# for each in range(len(fruits)):
#     if fruits[each] == 'cherry':
#         fruits[each] = 'lemon'
# print(fruits)
# second approach With map and lambda function

# fruits = list(map(lambda item: item.replace('cherry', 'lemon' ), fruits))
# print(fruits)

# fruits.insert(1, 'lemon')
# print(fruits)
#
# fruits.append('lemon')
# print(fruits)

# new_fruits0 = ["lemon" if i == "cherry" else i for i in fruits]
# print(new_fruits0)


#Напишите программу, которая распечатает последний элемент исходного листа и последний элемент по алфавиту.
# print(fruits[-1])
# fruits.sort()
# print(fruits[-1])


#Напишите программу, которая распечатает количество элементов в листе
# count =0
# for i in fruits:
#     count += 1
# print(count)

#Напишите программу, которая проверяет есть ли элемент "orange" в листе
# if "orange" in fruits:
#     print('true')
# else:
#     print('false')


#Напишите программу, которая удаляет три произвольных элемента из листа
# и распечатывает средний из удаленных элементов, если их расположить в алфавитном порядке.
# random_fruit = []
# for i in range(0, 3):
#     random_index = random.randint(0, len(fruits)-1)
#     random_fruit.append(fruits[random_index])
#     fruits.remove(fruits[random_index])
# print(random_fruit)
# random_fruit.sort()
# print(random_fruit)

# Напишите программу, которая изменит год выпуска на текущий
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1966
# }
# for each in car:
#     car['year'] = datetime.now().year
# print(car)

#Напишите программу, которая добавит информацию о цвете машины и присвойте значение цвета “red”
#
# car['color'] = 'red'
# print(car)

#Напишите программу, удаляющую информацию о модели автомобиля
#Ожидаемый результат
# del car['model']
# print(car)

#Напишите программу, удаляющую всю информацию из словаря.
#Ожидаемый результат:
# car =	{}
# car.clear()
# print(car)

#Напишите программу, которая возьмет произвольное целое число от 0 до 10
# и напечатает "It is long list", если в листе больше элементов, чем выбранное случайное число.
# random_num = random.randint(0, 10)
# print(f'Random numer: {random_num}')
# if len(fruits) > random_num:
#     print(f'It is long list')

#Напишите программу, которая возьмет произвольное целое число от 0 до 10
# и напечатает "Hello World", если число элементов в листе не равно выбранному случайному числу.
# random_num = random.randint(0, 10)
# print(f'Random number: {random_num}')
# if len(fruits) != random_num:
#     print(f'Hello World')

#Напишите программу, которая возьмет произвольное целое число от 0 до 10
# и напечатает "Yes", если число элементов в листе равно выбранному случайному числу,
# а если нет, распечатает “No”.
# random_num = random.randint(0, 10)
# print(f'Random number: {random_num}')
# if len(fruits) == random_num:
#     print(f'Yes')
# else:
#     print(f'No')

#Напишите программу, которая возьмет произвольное целое число от 0 до 10
# и напечатает "Bingo", если число элементов в листе равно выбранному случайному числу,
# "It is long list", если в листе больше элементов и “It is short list” если элементов меньше.

# random_num = random.randint(0,10)
# # print(f'Random number: {random_num}')
# if random.randrange(0, 10) == len(fruits):
#   print(f'Bingo')
# elif len(fruits) > random.randrange(0, 10):
#   print(f'It is a long list')
# else:
#   print(f'It is a short list')

# Заданы четыре числа a, b, c и d. Напишите программу, которая "Great equality",
# если a равно b и с равно d. А в противном случае программа напечатает “Oops!”
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))
# d = int(input('Enter d: '))
#
# if a == b and c == d:
#   print('Great equality!')
# else:
#   print ('Oops!')


# Напишите программу, которая создаст лист из четырех произвольных целых чисел от 0 до 10 и печатает "Success",
# если первый элемент больше последнего или второй элемент больше третьего.
# Если ни одно из условий не выполнено, то программа печатает “Failure”

# random_list= []
# for i in range(0, 4):
#   random_index = random.randint(0, 10)
#   random_list.append(random_index)
# print(random_list)
# if random_list[0] > random_list[-1] or random_list[1] > random_list[2]:
#   print('Success')
# else:
#   print('Failure')

# Напишите программу, которая создаст лист из семи произвольных целых чисел от 0 до 10
# и печатает "Success", если третий элемент листа больше первого и меньше последнего.
# Если ни одно из условий не выполнено, то программа печатает “Failure”

# random_list = []
# for i in range(0, 8):
#   random_index = random.randint(0, 10)
#   random_list.append(random_index)
# print(random_list)
# if random_list[2] > random_list[0] and random_list[2] < random_list[-1]:
#   print('Success')
# else:
#   print('Failure')

# Напишите программу, которая печатает произвольные числа в диапазоне от 0 до 20 до тех пор,
# пока значение случайного числа не станет меньше 3.
# Пусть программа напечатает сообщение, чему равно число из-за которого она прекратила выполнение.

# random_num = random.randint(0, 20)
# while(random_num > 3):
#   random_num = random.randint(0, 20)
# print(random_num)

#Напишите программу, которая выбирает произвольное целое число в диапазоне от 5 до 15,
# а затем печатает последовательность чисел от 1 до 20 (включительно) за исключением выбранного числа.

# random_num = random.randint(5, 15)
# print(f"random number: {random_num}")
# for i in range(5, 16):
#   if random_num == i:
#     continue
#   print(i)

#Напишите программу создающую список автомобилей в Вашем гараже (не меньше трех) (возможно вымышленном).
# Для каждого автомобиля должна храниться следующая информация: марка, модель, цвет, год выпуска.
# Программа должна распечатать цвет самой старой машины.

# cars= []
# car ={
#   'brand':'toyota',
#   'model': 'rav4',
#   'color': 'white',
#   'year': '2014'
# }
# cars.append(car)
# car ={
#   'brand':'mazda',
#   'model': 'cx5',
#   'color': 'blue',
#   'year': '2010'
# }
# cars.append(car)
# car ={
#   'brand':'lexus',
#   'model': 'mx200',
#   'color': 'red',
#   'year': '2020'
# }
# cars.append(car)
# # print(f'My garage of the cars: {cars}')
# # for each in cars:
# #   print(cars)
# cars_years = sorted(cars, key=lambda k: k['year'])
# print(cars_years)
# print(cars_years[0]['color'])


fruits = ["apple", "cherry", "orange", "kiwi", "melon", "banana",  "mango"]
# Напишите программу, которая каждый элемент отдельно, за исключением “banana”
# for each in fruits:
#   if each == 'banana':
#     continue
#   print(each)

# Напишите программу, которая будет печатать все фрукты, пока не дойдет до “kiwi”. А затем прекратит работу.

# for each in fruits:
#   if each == 'kiwi':
#     break
#   print(each)

# Напишите функцию my_sum, которая принимает два параметра и возвращает их сумму
# def twoSum(num1, num2):
#   return num1 + num2
# print(twoSum(178, 123))

# Напишите функцию my_new_sum, которая принимает любое число параметров и возвращает их сумму.

# def my_sum(*args):
#   summ = 0
#   for each in args:
#     summ = summ + each
#   return summ
# print(my_sum(12, -23, 0, 89, 77))

# Напишите программу, в которой есть функция, принимающая перечень людей с указанием их возраста
# и возвращающая возраст самого старшего.
# def oldest_age_bubble(*args, age_key):
#   ages = []
#   # print(len(args))
#   age_curr = args[0][age_key]
# #   bubble sort
#   for i in args:
#     if i[age_key]> age_curr:
#       print(i[age_key])
#       ages = i
#   return ages
#
# persons = []
# person={
#     "First Name": "Alex",
#     "Last Name":  "Popov",
#     "Age": 68
# }
# persons.append(person)
#
# person = {
#     "First Name": "Elena",
#     "Last Name":  "Boden",
#     "Age": 45
# }
# persons.append(person)
# person = {
#     "First Name": "Jack",
#     "Last Name":  "Little",
#     "Age": 25
# }
# persons.append(person)
#
# person = {
#     "First Name": "Nina",
#     "Last Name":  "McDonald",
#     "Age": 80
# }
# persons.append(person)
# # print(persons)
# print(oldest_age_bubble(*persons, age_key = 'Age'))
