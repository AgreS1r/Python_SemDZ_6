# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = [a1 + (i-1)*d for i in range(1, n+1)]
print(progression)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

# Пример использования функции
lst = [1, 5, 8, 4, 3, 9, 2]
min_val = 3
max_val = 7
indexes = find_indexes(lst, min_val, max_val)
print(f"Индексы элементов списка, значения которых находятся в диапазоне [{min_val}, {max_val}]: {indexes}")