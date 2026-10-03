#Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней
while True:
    user_input = input("Введите массу в килограммах (или 'exit' для выхода): ")

    if user_input == 'exit':
        print("Выход из программы.")
        break

    try:
        m = int(user_input)
        print("Целых тонн:", m // 1000)
        break
    except ValueError:
        print("Ошибка: введите корректное число")