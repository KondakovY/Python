"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
"""
class ListError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.l = []

    def check_value(self):
        global user_list
        while True:
            try:
                try:
                    user_list = int(input('Введите число: '))
                    ex = input(f'Корректное значение, число "{user_list}" добавлено в список. Для продолжения ввода '
                               f'нажмите Enter/конец ввода q: ').lower()
                    self.l.append(user_list)
                    if ex == 'q':
                        print(self.l)
                        break
                except ValueError:
                    raise ListError
            except ListError:
                ex = input(f"Некорректное значение (не число). Для продолжения ввода нажмите Enter/конец ввода q: ").lower()
                if ex == 'n':
                    print(self.l)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()
