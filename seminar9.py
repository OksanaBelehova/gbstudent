# 1. Создать класс, описывающий человека: имя, фамиля, возраст
# создать экземпляр и вывести информацию о человеке
# 2. Доработать, чтобы вся инфа о человеке была доступна при вызове str над экземпляром
# 3. Доработать метод greet, вызов которого будет выводить в консоль информацию о человеке в формате
# "Привет! Меня зовут Петров Василий, мне 12 лет"
# 4. Добавить атрибут grades, в котором будет хранится список оценок 
# Создать список учеников, заполняя оценки случайными числами
# И вывести информацию о них в порядке убывани среднего балла
# Заполнение оценок и подсчет среднего балла вынести в отдельные методы

# from statistics import mean
# class Human:
#     def __init__(self,name, surname, age, grades:list):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = grades

#     def __str__(self):
#         return f'{self.name}, {self.surname}, {self.age}, {self.grades}'
#     def greet(self):
#         print(f"Привет! Меня зовут {self.surname} {self.name}, мне {self.age} лет")
#     def sred_bal(self):
#         sred = mean(self.grades)
#         return(sred)
#     def __repr__(self) -> str:
#         return f'{self.surname} {self.name} {self.sred_bal()}'
#     def add_grade(self):
#         import random
#         random_grade = random.randint(2,5)
#         self.grades.append(random_grade)
    
# ivan = Human("Иван","Иванов",20,[4,4,4,4,4,4,4,])
# maks = Human("Макс","Коротин",15,[3,3,3,3,3,3,3,])
# vitya = Human("Витя","Никифоров",12,[5,5,5,5,])
# alex = Human("Алекс","Грин",18,[3,2,4,2,3])
# peoples = [ivan, maks, vitya, alex]

# new_peop = sorted(peoples,key=lambda x: x.sred_bal(),reverse=True)

# print(ivan)
# ivan.greet()
# print(ivan.sred_bal())
# print(new_peop)
# for item in peoples:
#     item.add_grade()
# print(new_peop)
# print(ivan)
# print(maks)
# print(vitya)
# print(alex)

# 5. Создайте класс прямоугольник Rectangle
# Метод __init__ принимает две точки - левый верхний и правый нижний угол
# Каждая точкапредставлена экземпляром класса Point
# Реализуйте методы вычисления площади и периметра прямоугольника
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,left_up:Point,right_down:Point):
        self.left_up = left_up
        self.right_down = right_down
    def get_perimetr(self):
        return(abs(self.left_up.x - self.right_down.x) + abs(self.left_up.y - self.right_down.y))*2
    def get_square(self):
        return(abs(self.left_up.x - self.right_down.x) * abs(self.left_up.y - self.right_down.y))
    def has_point(self):
        point_x = int(input('x='))
        point_y = int(input('y='))
        if self.left_up.x <= point_x <= self.right_down.x and self.left_up.y <= point_y <= self.right_down.y:
            return True
        else:
            return False
point1 = Point(1,1)
point2 = Point(10,10)
rect = Rectangle(point1,point2)
# print(rect.left_up.x)
print(rect.get_perimetr())
print(rect.get_square())
# 6. Добавте в класс Rectangle метод has_point
# Метод принимает точку на плоскости и возвращает true, 
# если точка находится внутри прямоугольника и false в противоположном случае
print(rect.has_point())