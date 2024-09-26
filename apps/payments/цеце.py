#point = 0
#while point<=10:
 #   print(f"количество очков: {point} ")
 #   point +=1

import random

number_bot = random.randint(1,10)
flag = True
count = 0
while flag:
    number_user = int(input("Введите число"))
if number_user < number_bot:
    print("загаданное число больше")
elif number_user > number_bot:
    print("загаданное число меньше")
else:
    print("Вы угадали число")
    count +=1
    print(count)
if count == 10:
    print("ура победа")

    