"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

Task_1 = 'File/Task1.txt'

with open(Task_1, 'w', encoding='UTF-8') as f:

    while True:
        s = input('Введите строку или ввод пустой строки: ')
        if not s:
            break
        f.write(f'{s}\n')
