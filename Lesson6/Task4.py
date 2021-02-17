"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Движение')

    def stop(self):
        print('Остановка')

    def turn(self, direction):
        print(f'Поворот: {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости: {self.speed}')
        else:
            print(f'Скорость: {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости: {self.speed}')
        else:
            print(f'Скорость: {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

work_car = WorkCar(speed=0, color='blue', name='Fiat Fuso')
work_car.go()
work_car.speed = 30
work_car.show_speed()
work_car.turn('Направо')
work_car.speed = 80
work_car.show_speed()
work_car.stop()
