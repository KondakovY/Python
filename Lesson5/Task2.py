"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

f = open('File/Task_2.txt', 'r', encoding='UTF-8')
line = 0
for i in f:
    line += 1
    flag = 0
    word = 0
    for a in i:
        if a != ' ' and flag == 0:
            word += 1
            flag = 1
        elif a == ' ':
            flag = 0

    print(f'{i} Количество символов в строке: {len(i)}, Количество слов: {word}')

print(f'Количество строк: {line}')
f.close()
