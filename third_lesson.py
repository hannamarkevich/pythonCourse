# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def input_number():
    while True:
        try:
            number = float(input("Input a number"))
            return number
        except ValueError:
            print("It's not a number, please, try again")


def division(*nums):
    try:
        result = nums[0]/nums[1]
        return result
    except ZeroDivisionError:
        print("Zero Division")


print(division(input_number(), input_number()))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(name, surname, year, city, email, phone):
    print(f"User info: \n name: {name} {surname}\n year of birth: {year}\n city: {city} \n email: {email}\n phone: {phone}")


user_info("lkjdgsf", "sdfgsdf", 1234, "sdf", "sdfasd@ks.fd", 237219258765)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def two_max_elements_sum(*args):
    result = 0
    if args.count(min(args)) > 1:
        print("2 or more equals numbers, cannot find correct decision")
        return None
    for element in args:
        if element != min(args):
            result += element
    return result


print(two_max_elements_sum(-15, -5, 56))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def pow_func(x, y):
    return x ** y


def pow_func_second(x, y):
    result = 1
    for i in range(abs(y)):
        result /= x
    return result


print(pow_func_second(53, -3), pow_func(53, -3))


#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после
# нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_func():
    special_symbol = '='
    result = 0
    is_last_string = False
    while not is_last_string:
        number_string = input("Enter numbers string: ")
        is_last_string = special_symbol in number_string
        number_string = number_string.split("=")[0]
        for number in number_string.split():
            result += int(number)
    return result


print(sum_func())

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(text):
    return text.capitalize()


def int_func_second(text):
    result = list(text)
    result[0] = result[0].upper()
    return ''.join(result)


def my_func(sentence):
    result = ""
    for word in sentence.split():
        result = result + int_func(word) + " "
    return result


print(my_func("skjdf.kjsdhfksdjhfs dksdf df sfhsskfhs  f"))

