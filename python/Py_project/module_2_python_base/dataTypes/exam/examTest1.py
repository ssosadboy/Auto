# class Product:
#     def __init__(self,name,price,category,stock):
#         self.name = name
#         self.price = price
#         self.category = category
#         self.stock = stock

#     def get_info(self):
#         return f'Информация о товаре {self.name} - {self.price} ,{self.stock}'

#     def is_available(self):
#         return self.stock

#     def reduce_stock(self,amount):
#         self.stock -= amount
#         return self.stock

#     def add_stock(self, amount):
#         self.stock += amount
#         return self.stock

# class ShoppingCart:

#     def __init__(self, customername):
#         self.customername = customername
#         self.items = {}
#         self.total_amount = 0

#     def add_item(self, product, quantity):
#         if product in self.items:
#             self.items[product] += quantity
#         else:
#             self.items[product] = quantity

#     def remove_item(self, product_name):
#         for product in self.items:
#             if product.name == product_name:
#                 del self.items[product]
#                 break
#     def calculate_total(self):
#         self.total_amount = 0
#         for product, quantity in self.items.items():
#             self.total_amount += product.price * quantity
#         return self.total_amount


#     def get_cart_info(self):
#         info = f"Корзина {self.customername}:\n"
#         for product, quantity in self.items.items():  # ← цикл по всем товарам
#             info += f"{product.name} - {quantity} шт.\n"
#         return info

#     def checkout(self):
#         for product, quantity in self.items.items():  # ← уменьшаем stock
#             product.reduce_stock(quantity)
#         self.items.clear()  # ← скобки! Это вызов метода
# # Тестирование должно работать примерно так:

# # Создаем товары
# laptop = Product("Ноутбук", 75000, "Электроника", 5)
# mouse = Product("Мышь", 2500, "Электроника", 20)
# book = Product("Python для начинающих", 1200, "Книги", 10)

# # Создаем корзину
# cart = ShoppingCart("Анна Петрова")

# print("=== Добавляем товары в корзину ===")
# cart.add_item(laptop, 1)
# cart.add_item(mouse, 2)
# cart.add_item(book, 3)

# print(cart.get_cart_info())

# print(f"\n=== Общая сумма ===")
# total = cart.calculate_total()
# print(f"К оплате: {total}₽")

# print(f"\n=== Оформляем заказ ===")
# cart.checkout()

# print(f"\n=== Проверяем остатки на складе ===")
# print(laptop.get_info())
# print(mouse.get_info())
# print(book.get_info())

# class Task:
#     def __init__(self, title):
#         self.title = title
#         self.status = 'сreate'      # новая задача — не начата
#         self.owner = None            # никому не назначена

#     def start(self):
#         if self.owner is None:
#             return f'Задачу "{self.title}" нельзя начать — она никому не назначена'
#         self.status = 'process'
#         return f'Задача "{self.title}" открыта, статус: {self.status}'

#     def complete(self):
#         if self.status != 'process':
#             return f'Задачу "{self.title}" нельзя завершить — она не в работе'
#         self.status = 'complete'
#         return f'Статус задачи "{self.title}" изменился — {self.status}'

#     def assign_to(self, developer):
#         self.owner = developer
#         return f'Задача "{self.title}" назначена на {developer.name}'


# class Project:
#     def __init__(self, epic, link):
#         self.epic = epic
#         self.link = link
#         self.tasks = []              # список задач проекта

#     def add_task(self, task):
#         self.tasks.append(task)
#         return f'Задача "{task.title}" добавлена в проект "{self.epic}"'

#     def get_progress(self):
#         if not self.tasks:
#             return 0
#         done = sum(1 for t in self.tasks if t.status == 'complete')
#         return round(done / len(self.tasks) * 100, 2)


# class Developer:
#     def __init__(self, name):
#         self.name = name
#         self.tasks = []              # список задач разработчика

#     def take_task(self, task):
#         task.assign_to(self)
#         task.start()
#         self.tasks.append(task)
#         return f'{self.name} взял задачу "{task.title}"'

#     def complete_task(self, task):
#         if task not in self.tasks:
#             return f'{self.name} не может завершить задачу "{task.title}" — она не его'
#         result = task.complete()
#         return result

#     def get_workload(self):
#         # количество задач в работе (не завершённых)
#         return sum(1 for t in self.tasks if t.status != 'complete')


# project = Project('Автоматизация', 'https://jira.example.com/PROJ-1')
# kirill = Developer('Кирилл')
# anna = Developer('Аня')

# t1 = Task('Написать тесты API')
# t2 = Task('Настроить CI/CD')
# t3 = Task('Документация')

# project.add_task(t1)
# project.add_task(t2)
# project.add_task(t3)

# kirill.take_task(t1)
# kirill.take_task(t2)
# anna.take_task(t3)

# kirill.complete_task(t1)
# anna.complete_task(t3)

# print(f'Прогресс: {project.get_progress()}%')
# print(f'Нагрузка Кирилла: {kirill.get_workload()}, Ани: {anna.get_workload()}')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


# s = Student()
# s1 = Student('K',2,32)
# Попробуй создать объекты с неправильным количеством аргументов:
# 1. Создай Person только с одним аргументом
# 2. Создай Student без аргументов
# 3. Создай Student с тремя аргументами
# Внимательно посмотри, в каком классе Python показывает ошибку в каждом случае
