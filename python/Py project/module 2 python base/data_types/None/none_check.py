username = None
if username is None:
    username = 'Гость'
    print(username)

else:
    print('Не найден')

def greet_user(name):
    # Проверяем, если name равно None, заменяем на "Аноним"
    if name is None:
        name = "Аноним"
    
    # Выводим приветствие
    print(f"Привет, {name}!")

# Тестируем функцию
greet_user(None)           # Передаём None
greet_user("Кирилл")       # Передаём имя

# Создаём словарь с ключами name, age, email
user_info = {
    "name": "Кирилл",
    "age": 25,
    "email": None  # Изначально email не указан
}

# Проверяем значение email
if user_info["email"] is None:
    user_info["email"] = "не указан"

# Выводим обновлённый словарь
print(user_info)