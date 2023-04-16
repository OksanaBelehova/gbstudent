# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# k = int(input())
# last_sum = []
# for i in range(k):
#     sum = 0
#     for j in range(1,i):
#         if i%j==0:
#             sum+=j
#     last_sum.append([i,sum])
# # print(last_sum)
# res = []
# for start in range(len(last_sum)):
#     for end in range(start+1,len(last_sum)):
#         if last_sum[start][0]==last_sum[end][1] and last_sum[start][1]==last_sum[end][0]:
#             res.append([last_sum[start][0],last_sum[end][0]])
# print(*res)



# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# a = [int(input()) for i in range(int(input()))]
# b = [int(input()) for j in range(int(input()))]
# c = [i for i in a if i not in b]

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# a = [int(input()) for i in range(int(input()))]
# print(a)
# d = len([a[i] for i in range(1,len(a)-1) if a[i-1]<a[i]>a[i+1]])
# count = 0
# for i in range(1,len(a)-1):
#     if a[i-1]<a[i]>a[i+1]:
#         count+=1
# print(count,d)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2
list_1 = [1, 2, 3, 2, 3]
count=0
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i]==list_1[j]:
            count+=1
print(count)