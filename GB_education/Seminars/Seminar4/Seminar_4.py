# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

word = 'a a a b c a a d c d d'

# word = input().split()

letterArr = word.split()
print(letterArr)
result = {}
for i in letterArr:
    if i in result:
        print(f'{i}_{result[i]}', end = ' ')
    else:
        print(i, end = ' ')
    result[i] = result.get(i, 0) + 1
print()
print(result)
print()

# ------------------
# получили строку
text = "a a a b c a a d c d d"
# сосдаем спиок из строки разделителем служит пробел
text_lst = text.split()
# создаем новый пустой список
new_lst = []
# проходим по каждому элементу списка text_lst
for i in range(len(text_lst)):
    # если есть i-элемент в срезе о начала списка до i-элемента не включая его
    if text_lst[i] in text_lst[:i]:
        # в список new_lst добавляем элемент + "_" + срез списка из него берем количество элементов со значением i 
        new_lst.append(text_lst[i]+"_"+str(text_lst[:i].count(text_lst[i])))
    else:
        # если нет i-символа, то в конец списка new_lst добавляем i-символ
        new_lst.append(text_lst[i])
# печатаем объединение списка в строку

print(', '.join(new_lst))
# # ------------------

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# someText = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(someText.upper().split())))

# upperText = someText.upper()
# wordsArr = upperText.split()
# resultArr = set(wordsArr)
# print(len(resultArr))
# print(resultArr)


# ===================================================
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 

# Функция ввода целого числа >= 0,
# с аргументом текстового приглашения
# def inputCheck(message):
#     flag = True
#     while flag:
#         arg = input(message)
#         if arg.isdigit() and int(arg) >= 0:
#             arg = int(arg)
#             flag = False
#         if flag:
#             print('Не удалось распознать число')
#     return arg


# max_number = 0
# flag = True
# while flag:
#     number = inputCheck('Введите число (0 — конец последовательности): ')
#     if number == 0:
#         flag = False
#     if max_number < number:
#         max_number = number
# print(f'Максимальное число во введенной последовательности: {max_number}')


# n = int(input("Вводите число: "))

# max_number = -1
# while n != 0:
#     if max_number < n:
#         max_number = n
#     n = int(input("Число: "))

# print(f"Ответ: {max_number}")
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 
# ===============================================================

# доп*3.)Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.


# *доп2
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие:
# 111222334 -> 31322414
# aaabbbbbccd -> 3a3b2c1d

# Восстановление:
# 31322414 ->111222334
# 3a3b2c1d->aaabbbbbccd

list_1 = [12, 7, -1, 21, 0]
for i in list_1:
    print(i, end = " ") # вывод каждого элемента списка
print()
list_1 = [12, 7, -1, 21, 0]
for i in range(len(list_1)):
    print(list_1[i], end = " ") # вывод каждого элемента списка