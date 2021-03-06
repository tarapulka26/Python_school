# Задача-1:
# # Напишите небольшую консольную утилиту,
# # позволяющую работать с папками текущей директории.
# # Утилита должна иметь меню выбора действия, в котором будут пункты:
# # 1. Перейти в папку
# # 2. Просмотреть содержимое текущей папки
# # 3. Удалить папку
# # 4. Создать папку
# # При выборе пунктов 1, 3, 4 программа запрашивает название папки
# # и выводит результат действия: "Успешно создано/удалено/перешел",
# # "Невозможно создать/удалить/перейти"
#
# # Для решения данной задачи используйте алгоритмы из задания easy,
# # оформленные в виде соответствующих функций,
# # и импортированные в данный файл из easy.py
import sys
import os
choice = int (input ('Выберите пункт:\n'
                     '1. Перейти в папку\n'
                     '2. Просмотреть содержимое текущей папки\n'
                     '3. Удалить папку\n'
                     '4. Создать папку\n'
                     'Ваш выбор:'))
if choice == 1:
    ui_dir = input('Введите путь нужной директории:')

    try:
        os.chdir (ui_dir)
        cwd = os.getcwd ()
        print('Вы успешно перешли в ' , cwd)
    except FileNotFoundError:
        print('Не верно указан путь: ', ui_dir)

elif choice == 2:
    from Lesson05_easy import view as choice2
    choice2()

elif choice == 3:
    from Lesson05_easy import remove_path as choice3


elif choice == 4:
    from Lesson05_easy import new_path as choice4


