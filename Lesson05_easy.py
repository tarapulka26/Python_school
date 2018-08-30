# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
def new_path():
    try:
        for i in range (1 , 10):
            os.mkdir ("dir_" + str (i))
    except:
        print("Already exist")
    a = input ("enter something ")
    print(a)


def remove_path ():
    try:
        for i in range (1 , 10):
            os.rmdir ("dir_" + str (i))
    except:
        print("Already removed")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def view ():
    list = os.listdir()
    print(list)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file ():
    shutil.copy (r'Lesson05_easy', r'Lesson05_easy_copy')

