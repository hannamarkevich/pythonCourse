# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
something = input("Input a fruit: ")
number = input("Input a number: ")
number = int(number) + 18
print(f"Your psychological age is {number} and you look like {something}")


#  Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
#  и выведите в формате чч:мм:сс. Используйте форматирование строк.
seconds_number = int(input("Enter seconds number:"))
hours = seconds_number // (60 * 60)
minutes = (seconds_number - (hours * 60 * 60)) // 60
seconds_number = seconds_number - (hours * 60 * 60) - (minutes * 60)
result = "{:02}".format(hours) + ":" + "{:02}".format(minutes) + ":" + "{:02}".format(seconds_number)
print(result)


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input("Enter a digit: "))
number = 100 * number + (20 * number) + (3 * number)
print(f"Result is: {number}")


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Enter a number: "))
digit = 0
while number // 10 > 0:
    digit = digit if (digit > number % 10) else (number % 10)
    number = number // 10
print(digit)


# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Input a revenue value:"))
costs = int(input("Input costs value"))
profit = revenue - costs
if profit > 0:
    print(f"Profit is: {profit}")
    print(f"Profitability is: {profit/revenue}")
    size = int(input("Input company size: "))
    print(f"Profit per person is {profit/size}")
else:
    print("Unfortunately, it was a bad period")


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Input a: "))
b = int(input("Input b: "))
day = 1
while a < b:
    a = a * 1.1
    day += 1
print(f"Day is {day}")
