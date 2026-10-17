# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза.
while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: введите корректные числа")

product = a * b
if product < 0:
    product *= 8
else:
    product *= 1.5

print("Результат:", product)