# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# ======================================================================
def fill_array():
    element = int(input('Введите первый элемент массива: '))
    difference = int(input('Введите разность элементов: '))
    size = int(input('Введите  размер массива: '))
    array = []
    array.append(element)
    for i in range(1, size):
        array.append(array[i-1] + (size-1)  * difference)
    return array
def show_array(array):
    print(array)


# array = fill_array()
# show_array(array)


# ======================================================================
# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# ======================================================================
def fill_array_2(size):
    array = [int(input('Введите элемент массива: ')) for i in range(size)]
    return array
def find_interval(array, start, end):
    index_list = [i for i in range(len(array)) if min(start, end) <= array[i] <= max(start, end)]
    # for i in range(len(array)):
    #     if min(start, end) <= array[i] <= max(start, end):
    #         index_list.append(i)
    return index_list

size = int(input('Введите количество элементов массива: '))
array = fill_array_2(size)
print(array)
start = int(input('Введите начало диапазона: '))   
end = int(input('Введите конец диапазона: '))
index_list = find_interval(array, start, end)
print(index_list)
# ======================================================================