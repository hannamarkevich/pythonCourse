# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix_array):
        self.matrix_array = matrix_array
        self.height = len(matrix_array)
        self.width = len(matrix_array[0])

    def __str__(self):
        max_num_len = 0
        for i in range(self.height):
            if max(self.matrix_array[i]) > max_num_len:
                max_num_len = max(self.matrix_array[i])
        to_string = ''
        for i in range(len(self.matrix_array)):
            for j in range(len(self.matrix_array[0])):
                to_string = to_string + str(self.matrix_array[i][j]).rjust(len(str(max_num_len)), " ") + " "
            to_string = to_string + "\n"
        return to_string

    def __add__(self, other):
        if (self.height != other.height) | (self.width != other.width):
            raise Exception("Matrixes have different dimensions, use full_add method!")
        else:
            matrix_sum = []
            for i in range(self.height):
                matrix_sum.append([self.matrix_array[i][j] + other.matrix_array[i][j] for j in range(self.width)])
        return Matrix(matrix_sum)

    def __eq__(self, other):
        return self.matrix_array == other.matrix_array

    def full_add(self, other):
        height = max(self.height, other.height)
        width = max(self.width, other.width)
        result = []
        for i in range(height):
            result.append([0 for x in range(width)])
        for i in range(height):
            for j in range(width):
                try:
                    result[i][j] += self.matrix_array[i][j]
                except IndexError:
                    pass
                try:
                    result[i][j] += other.matrix_array[i][j]
                except IndexError:
                    pass
        return Matrix(result)


matrix = Matrix([[3, 6, 7], [67, 234, 2]])
matrix1 = Matrix([[3, 6, 2], [67, 234, 0]])
# print(matrix.full_add(matrix1))
print(matrix + matrix1)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
# для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes(ABC):
    STANDARD_SIZE = 6

    def __init__(self, size):
        self._size = size

    @abstractmethod
    def tissue_consumption(self):
        pass

    @property
    def size(self):
        try:
            if self._size > 0:
                return self._size
            else:
                return self.STANDARD_SIZE
        except TypeError:
            return self.STANDARD_SIZE


class Suite(Clothes):
    STANDARD_SIZE = 20

    def tissue_consumption(self):
        return 2 * self.size + 0.3


class Coat(Clothes):
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


print(Suite(-10).size)
print(Coat(10).tissue_consumption())


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В


class Cell:
    DEFAULT_CELLS_NUMBER = 1

    def __init__(self, numbers):
        self._numbers = numbers

    def numbers(self):
        result = self.DEFAULT_CELLS_NUMBER
        try:
            if int(self._numbers) > 0:
                result = int(self._numbers)
        except (TypeError, ValueError):
            pass
        return result

    def __add__(self, other):
        return Cell(self.numbers() + other.numbers())

    def __mul__(self, other):
        return Cell(self.numbers() * other.numbers())

    def __sub__(self, other):
        if self.numbers() > other.numbers():
            return Cell(self.numbers() - other.numbers())
        else:
            raise Exception('Operation is impossible!')

    def __truediv__(self, other):
        return Cell(self.numbers() // other.numbers())

    def __str__(self):
        result = " "
        for i in range(self.numbers()):
            result += " __"
        result += "\n "
        for i in range(self.numbers()):
            result += "|__"
        result += "|"
        return result

    def make_order(self, number_in_row):
        if number_in_row > self.numbers():
            print(str(self))
        else:
            str_to_print = ''
            for i in range(number_in_row):
                str_to_print += " __"
            str_to_print += "\n"
            for i in range(self.numbers() // number_in_row):
                for j in range(number_in_row):
                    str_to_print += "|__"
                str_to_print += "|\n"
            for i in range(self.numbers() % number_in_row):
                str_to_print += "|__"
            str_to_print += "|\n"
            print(str_to_print)


print(str(Cell(3) + Cell("sdf")))
(Cell(1000) / Cell(100)).make_order(7)
