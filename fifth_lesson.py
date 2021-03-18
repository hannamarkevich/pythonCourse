# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
import json
my_file = open("my_file.txt", "w+")
while True:
    file_line = input("Input some information: ")
    if file_line == "":
        break
    else:
        my_file.write(file_line + "\n")
my_file.close()


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

second_file = open("111.txt", "r")
line_count = 0
for line in second_file:
    line_count += 1
    print(f"There are {len(line.split())} in {line_count} line")
second_file.close()
print(f"There are {line_count} lines in ")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

workers_count = 0
salary_sum = 0
workers_file = open("workers.txt", "r")
for line in workers_file:
    workers_count += 1
    salary = int(line.split()[1])
    salary_sum += salary
    if salary < 20000:
        print(line.split()[0])
workers_file.close()
print(f"Average salary is {salary_sum/workers_count}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translations = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
numbers_file = open("numbers.txt", "r+", encoding="utf-8")
translations_file = open("translations.txt", "w+", encoding="utf-8")

for line in numbers_file:
    temp = line.split()
    translations_file.write(f"{translations.get(temp[0])} {(temp[1])} {temp[2]}\n")
translations_file.close()
numbers_file.close()

#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers_file = open("numbers_two.txt", "w+")
numbers_file.write("232 4 23 365 898 7 86785 3 235 76 878 34 567 2345 2 23 8 6 345345 345")
numbers_file.close()
numbers_file = open("numbers_two.txt", "r+")
number_sum = 0
for line in numbers_file:
    for num in list(map(int, line.split())):
        number_sum += num
print(number_sum)

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
# словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

schedule = open("schedule.txt", encoding="utf-8")
statistic = {}
bracket_sym = "("
for line in schedule:
    hours = 0
    for s in line.split():
        if s.find(bracket_sym) > 0:
            if s[:s.index(bracket_sym)].isdigit():
                hours += int(s[:s.index(bracket_sym)])
    statistic[line.split()[0]] = hours
print(statistic)

#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

firm_file = open("firms.txt", "r")
average_profit = 0
firms_count = 0
profit_dict = {}
profit_json = open("profit.json", "w")
for line in firm_file:
    firms_count += 1
    profit = int(line.split()[2]) - int(line.split()[3])
    profit_dict[line.split()[0]] = profit
    if profit > 0:
        average_profit += profit
    else:
        print("No profit, sorry")
profit_dict["average_profit"] = average_profit / firms_count
json.dump(profit_dict, profit_json)
firm_file.close()
profit_json.close()


