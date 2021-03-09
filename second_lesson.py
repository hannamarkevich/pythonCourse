# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [762, "7sdfsda", True, (1, 2, 3)]
for element in my_list:
    print(type(element))


# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

my_list = []
input_value = input("Input list element, at the end press Enter")
while input_value != "":
    my_list.append(input_value)
    input_value = input("Input list element, at the end press Enter")
print(my_list)
for i in range(len(my_list) // 2):
    my_list[2 * (i + 1) - 1], my_list[2 * (i + 1) - 2] = my_list[2 * (i + 1) - 2], my_list[2 * (i + 1) - 1]
print(my_list)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
try:
    month_number = int(input("Input month number: "))
except ValueError:
    month_number = ""
    print("It's not a number!")
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
if month_number in spring_list:
    print("It's a spring!")
elif month_number in summer_list:
    print("It's a summer!")
elif month_number in autumn_list:
    print("It's a autumn!")
elif month_number in winter_list:
    print("It's a winter!")
else:
    print("Something went wrong")

months = {"It's a summer!": month_number in (6, 7, 8), "It's a spring!": month_number in (3, 4, 5),
          "It's a winter!": month_number in (12, 1, 2), "It's a autumn!": month_number in (9, 10, 11),
          "Something went wrong": (month_number < 1) | (month_number > 12)}
for season in months.keys():
    if months.get(season):
        print(season)
        break

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

sentence = input("Input a sentence: ")
word_number = 1
for word in sentence.split():
    word = word[:10]
    print(f"{word_number}. {word}")


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [7, 5, 3, 3, 2]
number = int(input("Input a number: "))
position = 0
if rating_list[-1] >= number:
    rating_list.append(number)
else:
    while (rating_list[position] >= number) & (position < len(rating_list)):
        position += 1
    rating_list.insert(position, number)
print(rating_list)


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


def enter_int(name):
    value = 0
    while True:
        try:
            value = int(input(f"Input {name}: "))
            return value
        except ValueError:
            print(f"{name} should be integer, try again please")


goods = []
input_value = input("Press any value to add a new good (or 1 not to add):")
number = 1
while input_value != "1":
    goods.append((number, {}))
    goods[number - 1][1]["name"] = input("Enter a name:")
    goods[number - 1][1]["price"] = enter_int("price")
    goods[number - 1][1]["number"] = enter_int("number")
    goods[number - 1][1]["units"] = input("Enter units:")
    number += 1
    input_value = input("Press any value to add a new good (or 1 not to add):")
print(goods)

analytics = {}
for attribute in goods[0][1].keys():
    analytics[attribute] = set()
    for good in goods:
        analytics[attribute].add(good[1].get(attribute))
print(analytics)
