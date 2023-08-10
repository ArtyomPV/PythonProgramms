# =====================================================================================================
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
def solution1():
    from random import randint
    size = int(input("Input size of array N = "))
    # lst = [randint(0, elem+1) for i in range(size)]
    lst = [0] * size
    for i in range(len(lst)):
        lst.append(int(input('Input value of array`s element: ')))

    elem = int(input("Input a number X = "))
    count = 0
    
    for i in range(len(lst)):
        if lst[i] == elem:
            count += 1
    print(f" the number X is met {count} times")

# =====================================================================================================
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
def check_valid_int(text):
    num = (input(text))
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Inputed  not integer number") 
            num = (input(text))
    return num
def solution2():
    
    from random import randint
    size = check_valid_int("Input size of array N = ")
    elem = check_valid_int("Input a number X = ")
    lst = [e for e in range(size)]
    print(lst)
    closest = lst[0]
    for i in range(1, len(lst)):
        if elem == lst[i]:
            closest = lst[i]
        elif elem > lst[i] and lst[i] > lst[i-1]:
            closest = lst[i]
        elif elem > lst[i] and lst[i] < lst[i-1]:
            closest = lst[i-1]
    print(closest)
    
# =====================================================================================================
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12
def solution3():
    text  = input("Input a word ").upper()
    points = 0
    points_dict = {0:1,
                   1:2,
                   2:3,
                   3:4,
                   4:5,
                   5:8,
                   6:10}
    
    lst_Eng = [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
               ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
               ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
               ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'],
               ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
               ['J', 'X', 'Ш', 'Э', 'Ю'],
               ['Q', 'Z', 'Ф', 'Щ', 'Ъ']]

    text_list = list(text)
    for i in range(len(lst_Eng)):
        for k in range(len(lst_Eng[i])):
            for j in range(len(text_list)):
                if text_list[j] == lst_Eng[i][k]:
                    points += points_dict[i]
    print(points)

# ====================================================
solution1()
# solution2()
# solution3()