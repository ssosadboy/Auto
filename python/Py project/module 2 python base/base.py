# # # # # # # # # # # # # # # # # # # FirstName = "segast"
# # # # # # # # # # # # # # # # # # # print(FirstName)

# # # # # # # # # # # # # # # # # # # say_me = 'My best friend'
# # # # # # # # # # # # # # # # # # # print(say_me)

# # # # # # # # # # # # # # # # # # # operate = 15
# # # # # # # # # # # # # # # # # # # print(operate ** 25)

# # # # # # # # # # # # # # # # # # number = 25
# # # # # # # # # # # # # # # # # # number += 2
# # # # # # # # # # # # # # # # # # print(number)
# # # # # # # # # # # # # # # # # # number -= 22
# # # # # # # # # # # # # # # # # # print(number)
# # # # # # # # # # # # # # # # # # number **= 3
# # # # # # # # # # # # # # # # # # print(number)

# # # # # # # # # # # # # # # # # equal = 5 == 5
# # # # # # # # # # # # # # # # # print(equal)

# # # # # # # # # # # # # # # # result = None
# # # # # # # # # # # # # # # # print(result is None)

# # # # # # # # # # # # # # # value1 = True
# # # # # # # # # # # # # # # value2 = 12345
# # # # # # # # # # # # # # # value3 = '123403434eweqw'
# # # # # # # # # # # # # # # print(type(value1))
# # # # # # # # # # # # # # # print(type(value2))
# # # # # # # # # # # # # # # print(type(value3))

# # # # # # # # # # # # # # # value = '213dsd'
# # # # # # # # # # # # # # # print(type(value))

# # # # # # # # # # # # # # fruits = ['яблоко', 'банан', 'вишня']

# # # # # # # # # # # # # # a = [1, 2, 3]
# # # # # # # # # # # # # # b = [4, 5, 6]
# # # # # # # # # # # # # # c = a + b
# # # # # # # # # # # # # # assert len(c) == len(a + b) , f'Ошибка'
# # # # # # # # # # # # # # print(c)

# # # # # # # # # # # # # numbers = [10, 20, 40, 50]
# # # # # # # # # # # # # numbers.insert(2, 30)
# # # # # # # # # # # # # print(numbers)
# # # # # # # # # # # # # numbers.clear()
# # # # # # # # # # # # # print(numbers)

# # # # # # # # # # # # value = [
# # # # # # # # # # # #     [1, 2, 3] ,
# # # # # # # # # # # #     ["a", "b", "c"],
# # # # # # # # # # # #     [True, False]
# # # # # # # # # # # # ]
# # # # # # # # # # # # resultB = value[1][1]
# # # # # # # # # # # # assert resultB == 'b', f'ошибка'
# # # # # # # # # # # # print(resultB)
# # # # # # # # # # # # last_item = value[0].pop()
# # # # # # # # # # # # assert last_item == 3 , f'Ошибка'
# # # # # # # # # # # # print(last_item)

# # # # # # # # # # # addList = {
# # # # # # # # # # #     'name': 'Kirill',
# # # # # # # # # # #     'surname': 'Viktorov',
# # # # # # # # # # #     'age': '23',
# # # # # # # # # # #     'email': '@mail.ru'
# # # # # # # # # # #     }
# # # # # # # # # # # newList = addList.copy()
# # # # # # # # # # # # assert addList == newList, f'ERROR'
# # # # # # # # # # # # print(newList)
# # # # # # # # # # # addList['phone'] = '92021'
# # # # # # # # # # # # print(addList)

# # # # # # # # # # # residencE = {
# # # # # # # # # # #     "residence": {
# # # # # # # # # # #         "country": "Thailand",
# # # # # # # # # # #         "city": "Phuket",
# # # # # # # # # # #         "district": "Thalang"
# # # # # # # # # # #     }
# # # # # # # # # # # }

# # # # # # # # # # # equal = residencE | addList
# # # # # # # # # # # print(equal["residence"]['city'])

# # # # # # # # # # corteg = (1, 2, '1sadas',  '%^*^&*' )
# # # # # # # # # # print(corteg)
# # # # # # # # # # # corteg[1] = 10
# # # # # # # # # # print(corteg[1])

# # # # # # # # # type1 = ({
# # # # # # # # #     'name':'k'
# # # # # # # # #     }, 2 )
# # # # # # # # # type2 = ({
# # # # # # # # #     'name':'k'
# # # # # # # # #     }, 2)
# # # # # # # # # assert type1 == type2, 'ERROR'
# # # # # # # # # print('True')

# # # # # # # # my_tuple = (1, 2, 3)
# # # # # # # # print(len(my_tuple))  # 3

# # # # # # # # values = (1, 2, 3, 4, 5)

# # # # # # # # a, b, *rest = values
# # # # # # # # print(a)     # Вывод: 1
# # # # # # # # print(b)     # Вывод: 2
# # # # # # # # print(rest)  # Вывод: [3, 4, 5]

# # # # # # # # x = 10
# # # # # # # # y = 20

# # # # # # # # coordinates = (x, y)  # Создаем кортеж из переменных
# # # # # # # # print(coordinates)  # Вывод: (10, 20)

# # # # # # # add = ("apple", "banana", "cherry", "apple")
# # # # # # # print(add.count("apple"))
# # # # # # # print(list(add).count("apple"))  # Преобразуем кортеж в список и считаем количество "apple"
# # # # # # # a , b, *rest = add
# # # # # # # tuple_2 = (a, b)
# # # # # # # assert list(tuple_2) == 2 , f'Ошибка'
# # # # # # # print(True)

# # # # # # list1 = [1, 2, 3]
# # # # # # list1 = set(list1)  # Преобразуем список в множество
# # # # # # print(list1)  # Вывод: {1, 2, 3}

# # # # # # list2 = {4, 5, 6, [7, 8]}
# # # # # # print(list2)

# # # # # list1 = {1, 2, 3, 4}
# # # # # list1.add(5)
# # # # # print(list1)
# # # # # a = list1.pop()
# # # # # print(a)

# # # # list1 = {1, 2, 3, 4}
# # # # list2 = {3, 4, 5, 6}
# # # # set = list1 ^ list2
# # # # print(set)

# # # list1 = [10, 20, 30, 40, 50]
# # # list2 = [20, 25, 30, 35, 40]
# # # print(set(list1) ^ set(list2))  # Вывод: {20, 30, 40}

# # r1 = range(2, 6, 2)
# # r2 = range(6, 2, -2)
# # print(list(r2))

# text = "Hello, world!"

# print('значение h: ', ord("h"))
# print('значение H: ', ord("H"))

