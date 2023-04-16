#list comprehension
# a = [i if i%2==0 else 0 for i in range(1,10)]
# print(a)

# enumerare
# a = [0, 2, 0, 4, 0, 6, 0, 8, 0]
# for indx,val in enumerate(a):
#     print(indx,val) 

# zip
# a = (1,2,3,4,5) #кортеж
# b = "abcd" #строка
# f = {45:"b",54:"c",87:"fr"} #словарь
# print(f.values())
# print(f.keys())
# print(f.items())
# for i in zip(a,b,f):
#     print(i)

#lamdda
# def summa(x,y):
#     return x+y

# summa = lambda x,y:x+y if x%2==0 else 0
# print(summa(8,6))

#map
# def pow(x):
#     return x**2
# a =[1,2,3,4,5,6]
# a  = list(map(pow, a))
# print(a)
# #a =[1,2,3,4,5,6]
# # a  = list(map(lambda x:x**2,a))
# #print(a)


#filter
# a =[1,2,3,4,5,6]
# a  = list(filter(lambda x: not x%2,a))
# print(a)

 #сортировка по ключу
# a = [(1,2,5),(3,0,4),(-5,-1,3),(5,-2,2)]
# #a.sort(key = lambda x: (x[1],x[2]), reverse=True)
# maxx = max(a,key=lambda x:x[2])
# print(maxx)

# Задача №47. Решение в группах
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
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok
# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation_values = list(map(transformation, values))
# if values == transformation_values:
#     print("ok")
# else:
#     print("fail")

# Задача №49. Решение в группах
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
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(orbits):
#     return max(orbits, key = lambda x: x[0]*x[1] if x[0]!=x[1] else -1)
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by(func,collection):
#     return len(list(filter(func,collection)))==0

# values = [0, 2, 10, 6,8,12,24] 
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")

# 2)Имеется упорядоченный список:
# a = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# # #
# # # Перебрать все элементы этого списка с помощью функций enumerate и 
# элементы, стоящие на главной диагонали (имеющие равные индексы со 
# списком и индексом

a = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
for indxOut,valOut in enumerate(a):
    for indxIn,ValIn in enumerate(valOut):
        if indxIn == indxOut:
            a[indxOut][indxIn] = 0
print(a)