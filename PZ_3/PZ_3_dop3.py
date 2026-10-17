# Ввести двузначное число. Если сумма цифр числа четная, то увеличить число на 2, в противном случае уменьшить на 2.
while True:
    try:
        number = int(input("Введите двузначное число: "))
        if number < 10 or number > 99:
            print("Ошибка: введите положительное двузначное число")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число")

digit_sum = number // 10 + number % 10
if digit_sum % 2 == 0:
    number += 2
else:
    number -= 2

print("Результат:", number)
