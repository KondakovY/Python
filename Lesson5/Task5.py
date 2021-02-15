"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('File/Task_5.txt', 'w', encoding='UTF-8') as f:
    numbers = input('Введите числа: ')
    f.write(numbers)


with open('File/Task_5.txt', 'r', encoding='UTF-8') as f:
    numbers_str = f.read()
    print(sum([int(numbers) for numbers in numbers_str.split()]))