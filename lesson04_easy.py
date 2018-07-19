# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка

import random
list1=[random.randint(-10,10)**2 for _ in range(10)]
print('list = ', list1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit1 = ["lemon","apple", "banana", "watermelon", "orange"]
fruit2 = ["peach", "lemon", "apple", "pear","melon", "banana"]
fruit3 = list(set(fruit1) & set(fruit2))
print (fruit3)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительныйx
# + Элемент не кратен 4
list1=[random.randint(-100,100) for _ in range(10)]
list2= [i for i in list1 if (i % 3== 0 and i > 0 and i % 4 != 0)]
print('list = ', list2)