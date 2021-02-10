"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
def func(hours, payment, bonus):
    return f'Зарплата составляет: {hours} * {payment} + {bonus} = {float(hours) * float(payment) + float(bonus)}'

_, hours, payment, bonus = argv
print(func(hours, payment,bonus))
