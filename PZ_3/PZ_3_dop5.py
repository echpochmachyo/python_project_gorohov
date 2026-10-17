# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
while True:
    try:
        a = int(input("Введите первое целое число: "))
        b = int(input("Введите второе целое число: "))
        break
    except ValueError:
        print("Ошибка: введите целые числа")

total = a + b
if total % 5 == 0:
    total += 1
else:
    total -= 2

print("Результат:", total)
