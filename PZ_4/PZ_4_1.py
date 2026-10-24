#Даны два целых числа А и В (А < Б). Найти произведение всех целых чисел от А до В включительно.
a, b = input("Введите число A: "), input("Введите число B: ")
while True:
    try:
        a = int(a)
        break
    except ValueError:
        print("Введите правильное число")
        a = input("Введите число A: ")
while True:
    try:
        b = int(b)
        break
    except ValueError:
        print("Введите правильное число")
        b = input("Введите число B: ")
if a < b:
    c = 1
    for i in range(a, b + 1):
        c *= i
    print("Произведение всех целых чисел от A до B включительно:", c)
else:
    print("Число A должно быть меньше числа B.")