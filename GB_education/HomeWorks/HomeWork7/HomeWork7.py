# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение
# Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам
# ================================================================================
def shortsolution_task1():
    """
    на выполнение короткой записи ушло более 2-х часов
    :return:
    """
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    text = "пара-ра-рам рам-пам-папам па-ра-па-да"
    text_split = text.split(" ")
    counter = (list(map(len, map(lambda text1: list(filter(lambda x: x in vowels, text1)), text_split))))
    print("Парам пам-пам" if all(x == counter[0] for x in counter) else "Пам парам")


def longsolution_task1():
    """
    решение этой задачи заняло не больше 20 минут
    :return:
    """
    text = "пара-ра-рам рам-пам-папам па-ра-па-да"
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    text_split = text.split(" ")
    counters = [0]*len(text_split)
    i = 0
    for word in text_split:
        for char in word:
            if char in vowels:
                # pass
                counters[i] += 1
        i += 1
    print("Парам пам-пам" if all(x == counters[0] for x in counters) else "Пам парам")


shortsolution_task1()
longsolution_task1()
# ================================================================================
# Задача 36: Напишите функцию print_operation_table
# (operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет
# с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как , например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
# ================================================================================
def solution_task2():
    def do_operation(operation, a=6, b=6):
        for x in range(1, a+1):
            for y in range(1, b+1):
                print("%2d" %operation(x, y), end=" ")
            print()
    do_operation(lambda x, y: x*y)


solution_task2()
# ================================================================================