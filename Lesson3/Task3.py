"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    q = [a, b, c]
    q.remove(min(a, b, c))
    return sum(q)

print(my_func(8, 9, 3))

#Простой вариант для трёх элементов
#def my_func(a, b, c):
#    if a < b and a < c:
#        return b + c
#    elif b < a and b < c:
#        return a + c
#    elif c < a and c < b:
#        return a + b
#
#print(my_func(7, 5, 8))
