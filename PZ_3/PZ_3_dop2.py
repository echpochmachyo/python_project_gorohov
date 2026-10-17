# Ввести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число")

if number % 2 == 0:
    number /= 4
else:
    number *= 5

print("Результат:", number)
