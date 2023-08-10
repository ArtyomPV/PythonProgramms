lst = [1, 2, 3]

lst2 = list(map(lambda x: x + 10, lst))
print(lst2)

orbits = [(1, 3), (2.5, 10), (7, 2), (6,6), (40, 40)]
def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x:(x[0]!=x[1])*x[0]*x[1])
print(find_farthest_orbit(orbits))

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# res = [(value, value ** 2) for value in data if value % 2 == 0]
# print(res)
# -----------------------------------------------------------------------------------
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
#     values = [1, 23, 42, ‘asdfg’]
#     transformed_values = list(map(trasformation, values))
#     if values == transformed_values:
#     print(‘ok’)
#     else:
#     print(‘fail’)
# Вывод:
#     ok
# ===================================================================================
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda value: value, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
print(transformed_values)
# ===================================================================================
# Планеты вращаются вокруг звезд по эллиптическим орбитам.

# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (7, 4)]
# def find_farthest_orbit(list_of_orbits):
a = list(map(lambda x: 3.14*x[0]*x[1] if x[0] != x[1] else 1, orbits))
indx = a.index(max(a))
print(a)
print(indx)
# =========================================================
# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                         Вывод:
# values = [0, 2, 10, 6]                         same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# =========================================================

# =========================================================
#41)Напишите программу на Python для поиска пересечения двух
# заданных массивов с помощью Lambda, filter.

# a1 = [1, 2, 3, 5, 7, 8, 9, 10]
# a2 = [1, 2, 4, 8, 9]
# =========================================================

# =========================================================
#2)Имеется упорядоченный список:

# A = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# #
# # Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.
# =========================================================

# =========================================================
#43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)
#
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.
#
# Выведете имена сотрудников, получившие нечетное id.
# =========================================================

# =========================================================
