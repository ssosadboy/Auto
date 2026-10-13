# # # # # # # # # # # # a = 10
# # # # # # # # # # # # b = 12
# # # # # # # # # # # # c = 30
# # # # # # # # # # # # # print(a - b)
# # # # # # # # # # # # # print(a + b)
# # # # # # # # # # # # # print(a * b)
# # # # # # # # # # # # # print(a / b)

# # # # # # # # # # # # # print(a > b)
# # # # # # # # # # # # # print(a < b)
# # # # # # # # # # # # # print(a == b)

# # # # # # # # # # # # # print(a + b == c)
# # # # # # # # # # # # # print(a * b < c)

# # # # # # # # # # # # # print(10 <= a <= 20)

# # # # # # # # # # # # num1 = float(input('Введите первое число: '))
# # # # # # # # # # # # num2 = float(input('Введите второе число: '))
# # # # # # # # # # # # operation = input('Выберите операцию (+, -, /, %, //, *): ')

# # # # # # # # # # # # if operation == '+':
# # # # # # # # # # # #     print(num1 + num2)

# # # # # # # # # # # # elif operation == '-':
# # # # # # # # # # # #     print(num1 - num2)

# # # # # # # # # # # # elif operation == '*':
# # # # # # # # # # # #     print(num1 * num2)

# # # # # # # # # # # # elif operation == '/':
# # # # # # # # # # # #     if num2 != 0:
# # # # # # # # # # # #         print(num1 / num2)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print('Ошибка: на ноль делить нельзя')

# # # # # # # # # # # # elif operation == '//':
# # # # # # # # # # # #     if num2 != 0:
# # # # # # # # # # # #         print(num1 // num2)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print('Ошибка: на ноль делить нельзя')

# # # # # # # # # # # # elif operation == '%':
# # # # # # # # # # # #     if num2 != 0:
# # # # # # # # # # # #         print(num1 % num2)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print('Ошибка: на ноль делить нельзя')

# # # # # # # # # # # # else:
# # # # # # # # # # # #     print('Ошибка: неверная операция')


# # # # # # # # # # # text = "Python is awesome!"
# # # # # # # # # # # # print(text.upper())
# # # # # # # # # # # textNew = text.replace('awesome', 'amazing')
# # # # # # # # # # # print(textNew)

# # # # # # # # # # # text = "Hello, Python!"
# # # # # # # # # # # # print(text[0:5])
# # # # # # # # # # # print(text[::2])

# # # # # # # # # # # pi = 3.14159
# # # # # # # # # # # rounded_pi = round(pi, 2)
# # # # # # # # # # # print(rounded_pi)

# # # # # # # # # # quote = "Python is easy and powerful!"
# # # # # # # # # # quote_new = quote.replace('easy', 'fun').replace('powerful', 'versatile')
# # # # # # # # # # print(quote_new)

# # # # # # # # # # name = "Alice"
# # # # # # # # # # age = 25
# # # # # # # # # # print(f'{name} is {age} years old.')

# # # # # # # # # data = "Price: 1234.5678 USD"
# # # # # # # # # data_slice = round(float(data[-13:-3]), 2)
# # # # # # # # # data_new = data.replace('1234.5678', str(data_slice))
# # # # # # # # # print(f'Rounded price: {data_new}')

# # # # # # # # fruits = ["apple", "banana", "cherry", "date"]
# # # # # # # # fruits.append('kiwi')
# # # # # # # # fruits.remove('banana')
# # # # # # # # print(fruits)

# # # # # # # person = {"name": "Alice", "age": 25, "city": "New York"}
# # # # # # # person['age'] = 26
# # # # # # # person['profession'] = 'Engineer'
# # # # # # # print(person)

# # # # # # numbers = (10, 20, 30, 40, 50)
# # # # # # print(numbers[1])

# # # # # colors = {"red", "blue", "green"}
# # # # # colors.add('yellow')
# # # # # colors.remove('blue')
# # # # # print(colors)

# # # # numbers = list(range(1, 21))
# # # # numbers_sum = sum(numbers)
# # # # newNumbers = [num for num in numbers if num % 3 == 0]
# # # # print(numbers)
# # # # print(newNumbers)

# # # numbers = []
# # # for num in range(1, 11):
# # #     if 0 < num <= 10:
# # #         numbers.append(num)
# # #     elif len.numbers == 10:
# # #         break
# # # print(numbers)

# # num = 10
# # while num >0:
# #     print('Обратный отсчет', num)
# #     num -= 1

# # print('Счет завершен')

# for i in range(5,6):
#     for j in range(1,11):
#         print(f'{i} * {j} = {i * j}')
#     print()

# MEGAPACKINGTASK

goods_and_prices = {
    'Зелье лечения': 100,
    'Зелье маны': 80,
    'Свиток скорости': 150,
    'Артефакт магии': 300,
}

userWant_item = input('Че надо, говори!?')
if userWant_item not in goods_and_prices:
    print('Это что ты сказал, прополощи свой рот, у меня такого нету!')
else:
    userWant_score = int(input('Cколько хочешь унести с собой дружок?'))

    if userWant_item in goods_and_prices:
        result = goods_and_prices[userWant_item] * userWant_score
        print(f'С тебя {result} золотых, давай деньги!')

        if result > 500:
            print('Хотя , хорошая закупка, дай подумать..')
            result *= 0.8
            print(f'Вай,вай, лови скидку 20% дружок, с тебя {result} золотых')
    else:
        print('Ограбить меня вздумал, поищи в другом месте!')
# sd