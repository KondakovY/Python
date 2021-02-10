"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import count, cycle

print('Итератор, генерирующий целые числа')
start = int(input('Начало генерации: '))
end = int(input('Введите число остановки: '))

counter = count(start)

for i in range(start, end + 1):
    print(next(counter))

cycler = cycle([1, 2, 3])
action = None
print('Итератор, повторяющий элементы некоторого списка, определенного зараннее')
print('Нажмите q, чтобы остановиться или любую другую кнопку, чтобы продолжить')
while action != 'q':
    print(next(cycler), end='')
    action = input()


