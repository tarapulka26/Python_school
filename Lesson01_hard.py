# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

name = input("Введите ваше имя:")
family = input("Введите вашу фамилию:")
age = int(input("Введите ваш возраст:"))
wage = int(input("Введите ваш вес:"))

if age<30 and 50<=wage<120:
    print (name,family,",Вы в отличном состоянии")
elif age>40 and (wage<50 or wage>120):
    print (name,family,",вам нужен лечебный осмотр!")
elif age>30 and (wage<50 or wage>120):
    print (name,family,",Надо начать ввести правильный образ жизни!")

else:
    print ("Формула не отражает реальной действительности и здесь используется только ради примера.")
