number = int(input("введите число: "))
if number %2 ==0:
    print:("{number} четное")
else:
    print:("{number} не четное")

age=int(input("введите возраст"))
if age <18 :
    print("несовершенно летний")
else:
    print("совершенно летний")


num1=int(input("введите 1 число"))
num2=int(input("введите 2 число"))
if num1 > num2:
    print(" больше")
else:
    print(" меньше ")


clock=int(input("введите время"))
if 0<clock<12:
    print("день")
else:
    print("ночь")


number=int(input("введите число"))
if number %2 ==0:
     print(" четное число")
else:
     print(" не четное число")


num= int(input(" введите оценку"))
if 0<num<30:
    print(" неудовлитворительно")
elif 30<num<60:
    print(" удовлитворительно")
elif 60<num<80:
    print("хорошо")
else:
    print("плохо")

number=int(input("введите время"))
if 0<number<5:
    print("утро")
elif 5<number<12:
    print("ночь")
elif 0<number<5:
    print("ночь")