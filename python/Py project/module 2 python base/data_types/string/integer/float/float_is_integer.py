
# number1 = 10.00
# number2 = 10.5 
# is_whole_number1 = number1.is_integer()
# is_whole_number2 = number2.is_integer()
# print(is_whole_number1, is_whole_number2)

num = float(input("Введите число: "))
result = num.is_integer()
if num.is_integer():
    print("Число целое")
else:
    print("Число не является целым")