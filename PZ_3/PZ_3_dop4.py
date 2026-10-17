# Дано целое число. Если оно является положительным, то прибавить к нему 20, в противном случае вычесть из него 5.
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число")

if number > 0:
    number += 20
else:
    number -= 5

print("Результат:", number)
