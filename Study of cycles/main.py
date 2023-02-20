# n = int(input())
# x = 1
# while x <= n:
#     print('*' * x)
#     x += 1

# Вывод суммы чисел
# x = 0
# n = int(input())
# while n != 0:
#     x += n
#     n = int(input())
# print(x)

# Минимальное делимое

# a = int(input())
# b = int(input())
# d = max(a,b)
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)


#Пропуски и продолжения

# while 1:
#     n = int(input())
#     if n < 10:
#         continue
#     elif n > 100:
#         break
#     else:
#         print(n)


#Таблица умножения

# a, b, c, d = (int(j)for j in input().split()) # можно вводить все в одну строку через пробел
# print (" ")
# for i in range (c, d + 1):
#     print ("  ", i, end=" ")
# print()
# for x in range(a,b + 1):
#     print(x, end= " ")
#     for y in range (c, d + 1):
#         print(" ", x * y, end=" ")
#     print()

#Среднее арифметическое чисел кратных 3

# a = int(input())
# b = int(input())
# sum = 0
# count = 0
# for i in range (a, b + 1):
#     if i % 3 == 0:
#         sum += i
#         count += 1
# sum = sum / count
# print(sum)

# str = "ATGC"
# for i in str:
#     print(i)
# print(str.count("T")) # функция сколько раз встречается в строке

# s = 'aTGcc';p = 'cc'

# print(s.upper())    # все символы большие
# print(s.lower())    # все маленькие
# print(s.count(p))   # сколько раз p встречается в s
# print(s.find(p))    # показывает индекс по которому p встречается в s
# print(s.find('A'))  # - 1 строка 'A' не входит в s
# print(s.replace('c', 'C')) # заменяет символы с на С


# процент от всей строки

# s = input()
# s = s.lower()
# countCG = s.count("c") + s.count("g")
# sum = countCG / len(s) * 100
# print(sum)

# s = 'abcdefghijk'
# print(s[3:6], end=" ")
# print(s[:6], end=" ")
# print(s[3:], end=" ")
# print(s[::-1], end=" ")
# print(s[-3:], end=" ")
# print(s[:-6], end=" ")
# print(s[-1:-10:-2], end=" ")


# кодировка строки

s = input()
n = ""
current = s[0]
count = 0
if len(s) == 1:
    n = s + str(1)
else:
    for i in s:
        if current == i:
            count += 1
        else:
            n += current
            n = n + str(count)
            current = i
            count = 1
    n += current
    n = n + str(count)
    print(n)