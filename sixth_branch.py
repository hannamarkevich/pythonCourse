# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
import time


class TrafficLight:

    def __init__(self, color):
        self._color = color

    def running(self):
        while True:
            if self._color == "red":
                timestamp = time.time()
                while time.time() - timestamp < 7:
                    print(self._color)
                self._color = "yellow"
            elif self._color == "yellow":
                timestamp = time.time()
                while time.time() - timestamp < 2:
                    print(self._color)
                self._color = "green"
            elif self._color == "green":
                timestamp = time.time()
                while time.time() - timestamp < 2:
                    print(self._color)
                self._color = "red"


TrafficLight("yellow").running()'''


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, mass, thickness):
        return self._width * self._length * thickness


print(Road(3, 4).mass_calculation(5, 6))


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе
# Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


pos = Position("asdasd", "yyyy", "werre", 23434, 3456)
print(f"Name {pos.get_full_name()}, salary {pos.get_total_income()}")


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые
# должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    SPEED_LIMIT = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("The Car starts to go")

    def stop(self):
        print("The Car is stopped")

    def turn(self, direction):
        print(f"The Car turns to {direction}")

    def show_speed(self):
        print(f"Speed is: {self.speed}")
        if (self.SPEED_LIMIT != 0) & (self.speed > self.SPEED_LIMIT):
            print("Attention!! Speed is too high!!!\n")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name, False)


class TownCar(Car):
    SPEED_LIMIT = 60

    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name, False)


class WorkCar(Car):
    SPEED_LIMIT = 40

    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)


TownCar(61, "asa", "kd").show_speed()
WorkCar(41, "asa", "kd").show_speed()
SportCar(1161, "asa", "kd").show_speed()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing started")


class Pen(Stationary):

    def draw(self):
        print("Pen starts drawing")


class Pencil(Stationary):

    def draw(self):
        print("Pencil starts drawing")


class Handle(Stationary):

    def draw(self):
        print("Handle starts drawing")


print(Handle("qwqw").draw())
