"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""

class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.warehouse_all = []
        self.warehouse = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за ед.: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.warehouse.append(self.my_unit)
            print(f'Текущий список -\n {self.warehouse}')
        except:
            return f'Ошибка ввода данных'

        print(f'Продолжение ввода Enter/выход из цикла Q')
        q = input(f'Введите значение: ')
        if q == 'Q' or q == 'q':
            self.warehouse_all.append(self.warehouse)
            print(f'Номенклатуры склада -\n {self.warehouse_all}')
            return f'Завершение работы'
        else:
            return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def func_print(self):
        return f'Использовался {self.numb} раз'


class Scanner(OfficeEquipment):
    def func_scan(self):
        return f'Использовался {self.numb} раз'


class Copier(OfficeEquipment):
    def func_copier(self):
        return f'Использовался {self.numb} раз'


unit_1 = Printer('hp', 180, 3, 7)
unit_2 = Scanner('Canon', 300, 6, 9)
unit_3 = Copier('Xerox', 450, 2, 4)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.func_print())
print(unit_2.func_scan())
print(unit_3.func_copier())
