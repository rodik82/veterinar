a=int(input("Введите число "))
if (a % 2 == 0) and (a > 0):
    print("Положительное четное число")
elif (a %2 != 0) and (a > 0):
    print("Положительное нечетное число")
    print("Число не является четным")
elif (a % 2 == 0) and (a < 0):
    print("Отрицательное четное число")
elif (a %2 != 0) and (a < 0):
    print("Отрицательное нечетное число")
    print("Число не является четным")
else:
    print("Нулевое число")