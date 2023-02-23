# Списки

# students= ['Ivan', 'Masha', 'Sasha']
# students.append('Olga') # добавление элемента
# students += ['Iurii', 'Kseniia'] # добавление элемента
# print(students)
# students.insert(1, 'Serafima') # вставляем на индекс нужный элемент
# print(students)
#
# students.remove('Iurii') # удаление первичного элемента
# print(students)
#
# del students[0] # удаление элемента по индексу
# print(students)
#
# if 'Olga' in students:
#     print('Yes') # поиск на соответствие
# if 'Valera' not in students:
#     print('No') # поиск на несоответствие
#
# ind = students.index('Masha') # возвращает индекс элемента
# print(ind)

# Сортировка списка

# order_sorted = sorted(students) # получаем новый отсортированный список
# print(order_sorted)
#
# students.sort() # сортируем сам список
# print(students)
# print(min(students)) # первый
# print(max(students)) # последний
#
# students.reverse() # сам список реверсирует
# rev = reversed(students) # новый реверсированный
#
# c = [1, 'A', 2]
# d = c
# c[0] = 42
# print(c)
# print(c)
# d[2] = 30
# print(c)
# print(d)

# a = [1, 2, 3]
# b = a
# print(b)
# # значения списка b?
#
# a[1] = 10
# print(b)
# # значения списка b?
#
# b[0] = 20
# print(a)
# # значения списка a?
#
# a = [5, 6]
# print(b)
# # значения списка b?


# Сумма строки

# f = [int(i) for i in input().split()]
# sumList = 0
# for i in f:
#     sumList += i
# print(sumList)

# Сумма соседей

# a = [int(i) for i in input().split()]
# b = []
# if len(a) == 1:
#     print(*a)
# else:
#     for j in range(len(a)):
#         if j == 0:
#             b.append(a[1] + a[-1])
#         elif j == len(a) - 1:
#             b.append(a[-2] + a[0])
#         else:
#             b.append(a[j - 1] + a[j + 1])
# print(*b) # выводит список

# Вывод встречающихся чисел

# a = [int(i) for i in input().split()]
# a.sort()
# b = []
# for i in range(len(a) - 1):
#     if a.count(a[i]) > 1:
#         if a[i] in b:
#             continue
#         b.append(a[i])
# print(*b)


# Квадраты введенных чисел
# total = 0
# mult = 0
# while mult >= 0:
#     current = int(input())
#     mult += current ** 2
#     total += current
#     if total == 0:
#         break
# print(mult)


# Вывод последовательности

# n = int(input())
# s = []
# if n == 0:
#     print()
# elif n == 1:
#     print(1)
# elif n == 2:
#     print(1, 2)
# else:
#     for i in range(n):
#         s += [i] * i
#         b = s[0:n]
#     print(*b)

# Вывод индексов числа

# list = [int(i) for i in input().split()]
# number = int(input())
# newList = []
# for i in range(len(list)):
#     if list[i] == number:
#         newList.append(i)
# if number not in list:
#     print("Отсутствует")
# else:
#     print(*newList)

# Шматрица (надо вывести матрицу из суммы соседних чисел)

# a = []
# b = []
# while True:
#     s = input()
#     if s == 'end':
#         break
#     a.append([int(i) for i in s.split()])
# b = [[0] * len(a[0]) for i in range(len(a))]
# for i in range(len(a)):
#     for j in range (len(a[0])):
#         b[i][j] = a[i-len(a)+1][j]+a[i-1][j]+a[i][j-len(a[0])+1]+a[i][j-1]
# for i in b:
#     print (*i)


# Спиральная матрица

n = int(input())  # размер матрицы
a = [[0] * n for i in range(n)]  # создание матрицы нужного размера, заполнена 0
count = 0  # количество заполненных ячеек
for i in range(n):   # заполнение 1 строки
    count += 1
    a[0][i] = count
j = 0   # указываем последнюю заполненную ячейку
i = n-1
n -= 1  # устанавливаем размер 1 блока 1 витка
while len(a)**2 != count:  #условие выхода из цикла
    for k in range(n):  #движение вниз
        j += 1
        count += 1
        a[j][i] = count  # заполнение матрицы
    for k in range(n):  #движение влево
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):  #движение вверх
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1): #движение вправо
        i += 1
        count += 1
        a[j][i] = count
    n -= 2    # обеспечиваем переход на внутренний виток
for i in range(len(a)):  #вывод полученной матрицы
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()