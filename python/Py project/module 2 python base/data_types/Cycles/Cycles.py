# # # # # # # # # # # # # numbers = [10, 20, 30, 40, 50]
# # # # # # # # # # # # # for number in numbers:
# # # # # # # # # # # # #     print('Число:', number)

# # # # # # # # # # # # sentence = "Hello, Python!"
# # # # # # # # # # # # for word in sentence:
# # # # # # # # # # # #     print('Буква:', word)

# # # # # # # # # # # name_age = {
# # # # # # # # # # #     'Alice': 35,
# # # # # # # # # # #     'Bob': 42,
# # # # # # # # # # #     'Charlie': 28
# # # # # # # # # # # }
# # # # # # # # # # # for name, age in name_age.items():
# # # # # # # # # # #     print( name, age)

# # # # # # # # # # count = 10
# # # # # # # # # # while count > 0:
# # # # # # # # # #     print('Обратный отсчёт:', count)
# # # # # # # # # #     count -= 1
# # # # # # # # # # print('Цикл завершён!')

# # # # # # # # # password = 12345
# # # # # # # # # userWord = 0
# # # # # # # # # while userWord != password:
# # # # # # # # #     userWord = int(input('Введите пароль: '))
# # # # # # # # #     if userWord != password:
# # # # # # # # #         print('Пароль неверный! Попробуйте ещё раз.')

# # # # # # # # # else:
# # # # # # # # #     print('Пароль верный!')

# # # # # # # # number = 0
# # # # # # # # while True:
# # # # # # # #     if number % 2 != 0:
# # # # # # # #         print('Нечётное число:', number)
# # # # # # # #     number += 1
# # # # # # # #     if number > 10:
# # # # # # # #         break

# # # # # # # integer = 0
# # # # # # # while True:
# # # # # # #     if integer < 50:
# # # # # # #         integer += 1

# # # # # # #     if integer >= 50:
# # # # # # #         print('Искомое число:', integer)
# # # # # # #         break

# # # # # # num = 0

# # # # # # while num < 20:
# # # # # #     num += 1

# # # # # #     if num % 3 != 0:
# # # # # #         continue

# # # # # #     print('Число кратное 3:', num)

# # # # # print('Имя\tДолжность\tЗарплата')
# # # # # print('Иванов\tМенеджер\t50000')
# # # # # print('Петров\tРазработчик\t70000')

# # # # numbers = [10, 0, 5, 2]

# # # # for num in numbers:
# # # #     try:
# # # #         result = 10 / num
# # # #         print(f"Результат деления: {result}")
# # # #     except ZeroDivisionError:
# # # #         print("Ошибка: Деление на ноль невозможно.")

# # # data = ["123", "abc", "456", None]

# # # for item in data:
# # #     try:
# # #         number = int(item)  # Попытка преобразования строки в число
# # #         print(f"Число: {number}")
# # #     except (ValueError, TypeError):
# # #         print(f"Ошибка: {item} не удалось преобразовать в число.")


# # ls = [10, 0, 5, "abc", 2]
# # for i in ls:
# #     try:
# #         result = 100/i
# #         print(f"Результат деления: {result}")
# #     except ZeroDivisionError:
# #         print("Ошибка: Деление на ноль невозможно.")
# #     except TypeError:
# #         print(f"Ошибка: Невозможно выполнить деление с типом {type(i).__name__}.")

# ls = ["123", "text", None, "456"]
# for i in ls:
#     try:
#         number = int(i)
#         print(f"Преобразованное число: {number}")
#     except (ValueError, TypeError):
#         print(f"Ошибка: Невозможно преобразовать {i} в число.")

ls = [(10, 5), (3, 0), (7, "str")]
for a, b in ls:
    try:
        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
    except TypeError:
        print(
            f"Ошибка: Невозможно выполнить деление с типом {type(b).__name__}.")
