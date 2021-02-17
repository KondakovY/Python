"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины
полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
#class Road:
#    def __init__(self, length, width):
#        self._length = length
#        self._width = width
#
#    def mass(self, weight, depth):
#        return self._length * self._width * weight * depth
#
#road = Road(20, 5000)
#print(road.mass(25, 5))

class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        total = self._length * self._width * self.weight * self.depth / 1000
        return print(f'Масса асфальта: {self._length} м * {self._width} м * {self.weight} кг * {self.depth} см = ',total, 'т')

road = Road(20, 5000, 25, 5)
road.mass()
