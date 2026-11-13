name = 'Сергей'
age = 28
greeting_f = f'Привет - меня зовут {name} и мне {age} лет'
print(greeting_f)

city = 'Москва'
temperature = 15.5
weather_format = 'Погода в {} сейчас {} градусов'.format(city, temperature)
print(weather_format)

product = 'ноутбук'
price = 54999 
product_info_percent = "Товар: %s, Цена: %d руб." % (product, price)
print(product_info_percent) 