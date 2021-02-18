"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
"""

class Cell:
    def __init__(self, atom):
        self.atom = atom

    def __add__(self, other):
        return Cell(self.atom + other.atom)

    def __sub__(self, other):
        if self.atom - other.atom <= 0:
            print(f'Недопустимое значение')
        return Cell(self.atom - other.atom)

    def __mul__(self, other):
        return Cell(self.atom * other.atom)

    def __truediv__(self, other):
        return Cell(self.atom // other.atom)

    def make_order(self, atom_row):
        list = ['◎' for _ in range(self.atom)]
        return '\n'.join([''.join(list[i:i+atom_row]) for i in range(0, len(list), atom_row)])


oc_1 = Cell(5)
print(f'Первая клетка:\n{oc_1.make_order(5)}')
oc_2 = Cell(7)
print(f'Вторая клетка:\n{oc_2.make_order(5)}')
oc_3 = oc_1 + oc_2
print(f'Третья клетка:\n{oc_3.make_order(5)}')
oc_4 = oc_3 / oc_1
print(f'Четвёртая клетка:\n{oc_4.make_order(5)}')
oc_5 = oc_1 * oc_4
print(f'Пятая клетка:\n{oc_5.make_order(5)}')
oc_6 = oc_5 - oc_4
print(f'Шестая клетка:\n{oc_6.make_order(5)}')