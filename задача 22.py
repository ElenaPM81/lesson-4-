# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого 
# множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('введите количество элементов первого множества:'))
numbers = set(input (f'введите  элементов {n}:'))
m = int(input('введите количество элементов второго множества:'))
numbers2 = set(input(f'введите  элементов {m}:'))
numbers3 = numbers.intersection(numbers2)
a = list(numbers3)
a.sort()
for i in a:
  print (i, end=', ')
