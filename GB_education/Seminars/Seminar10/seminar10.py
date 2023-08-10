import random 
#
# 1.Создать класс, описывающий человека.
# Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.
#
# 2.Доработать предыдущий класс, чтобы вся информация о человеке была
# доступна при вызове str над экземпляром.

class Human:

    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f"1Person: {self.last_name} {self.name}, age: {self.age}"

    def about(self) -> str:
        return f"2Person: {self.last_name} {self.name}, age: {self.age}"

    def greet(self) -> str:
        return f"Привет! Меня зовут {self.last_name} {self.name}, " \
               f"мне {self.age} лет"


person = Human('Ivanov', 'Ivan', 35)

# print(person)
# print(person.about())
# print(person.greet())

#
# 3.Добавить метод greet, вызов которого будет выводить в консоль
# информацию о человеке в формате "Привет! Меня зовут Петров Василий, мне 12 лет".
#

# 4.Добавить атрибут grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки случайными числами.
# и вывести информацию о них в порядке убывания среднего балла.
# Заполнение оценок и подсчёт среднего балла вынести в отдельные методы.
#



class Grade:

    def __init__(self) -> None:
        self.grades = list()

    def get_random_grades(self, number_grades: int) -> list:
        self.grades = [random.randint(2, 5) for _ in range(number_grades)]
        return self.grades

    def get_grade(self, grade: int) -> list:
        self.grades.append(grade)
        return self.grades

    def get_all_grades(self) -> list:
        return self.grades


class Student(Human):
    def __init__(self, name: str, last_name: str, age: int, grades: Grade) -> None:
        super().__init__(name, last_name, age)
        self.grades = grades
        self.grades_set = []

    def __repr__(self):
        return self.last_name

    def average_grades(self) -> float:
        return sum(self.grades.get_all_grades())/len(self.grades.get_all_grades())

    def set_grades(self, number_grades):
        self.grades_set = self.grades.get_random_grades(number_grades)
        return self.grades_set

    def get_grades(self):
        return self.grades_set


def main():
    points = Grade()

    student1 = Student("Ivan", 'Ivanov', 23, points)
    student2 = Student("Petr", 'Petrov', 20, points)
    student3 = Student("Grischa", 'Smirnov', 18, points)

    student1.set_grades(5)
    student2.set_grades(6)
    student3.set_grades(4)

    student1.average_grades()
    student2.average_grades()
    student3.average_grades()

    students = [student1, student2, student3]

    print(sorted(students, key=lambda x: x.get_grades()[1]))


main()

# print(sorted(students, key=lambda x: x.get_average()))

# 5. Создайте класс прямоугольник — Rectangle. Метод __init__
# принимает две точки — левый верхний и правый нижний угол.
# Каждая точка представлена экземпляром класса Point.
# Реализуйте методы вычисления площади и периметра прямоугольника.
#
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, dot1, dot2):
        self.dot1 = dot1
        self.dot2 = dot2
        self.length = self.dot1.x - self.dot2.x
        self.width = self.dot1.y - self.dot2.y

    def get_area(self):
        return self.length * self.width

    def get_perim(self):
        return (self.length + self.width) * 2

    def has_point(self, dot3):
        self.dot3 = dot3
        if self.dot2.x < self.dot3.x < self.dot1.x and self.dot2.y < \
                self.dot3.y < self.dot1.y:
            return True
        return False


dot1 = Dot(5, 5)
dot2 = Dot(2, 2)
dot3 = Dot(3, 3)
rect = Rectangle(dot1, dot2)
print(rect.get_area())
print(rect.get_perim())
print(rect.has_point(dot3))
# 6.Добавьте в класс Rectangle метод has_point.
# Метод принимает точку на плоскости и возвращает True,
# если точка находится внутри прямоугольника и False в противном случае.