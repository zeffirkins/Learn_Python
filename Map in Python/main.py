# МНОЖЕСТВА в Питоне
#
# s = set() # пусое множество
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} # заполненное множество
#
# print(basket)
# 'orange' in basket # конструкция для проверки наличия в множестве
#
# s.add('banana') # добавить в множество
# s.add('cola')
# print(s)
# s.remove('cola') # удалить из множества(если элемента нет - ошибка)
# s.discard('cola') # удаление без ошибки
# s.clear() # очистить множество
# len(s) # узнать количество элементов в множестве
#
# for x in basket:
#	print(x)


# СЛОВАРИ


#dict, {} # создание пустого словаря
# d = {'a': 10, 10:100} # словарь ключ:значение
# print(d['a'])
# print(d[10])
#
# bl ='a' in d #есть ли ключ в словаре
# d['b'] = 15 #добавление элемента
# print(d['b'])
# #d['c'] # получение значения по ключу(ошибка если нет его)
# d.get('b') # получение без ошибки
# del d['b'] # Удаление пары по ключу
# print(d.get('b'))

# изменяемы
# элементы не имеют порядка
# все ключи различны
# ключи не изменяемы

# d = {'C':14, 'A':12, 'T':9, 'G':18}
#
# for key in d:
# 	print(key, end=' ')# getting the keys in dictionary
# print()
# for key in d.keys():
# 	print(key, end=' ')# getting the keys in dictionary
# print()
# for key in d.values():
# 	print(key, end=' ')# getting the values in dictionary
# print()
# for key, value in d.items():
#	print(key, value, end=';') # getting the keys and values in dictionary

# Можно сопоставлять ключу не одно значение, а список

# task 1 adding element in dict
# d = {}
#
# def update_dictionary(d, key, value):
# 	if key in d:
# 		d[key] += [value]
# 	else:
# 		if key * 2 in d:
# 			d[key * 2] += [value]
# 		else:
# 			d[key * 2] = [value]
#
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

# task 2 print count word in string
# l = []
# d ={}
# l = input().lower().split()
# #print(l)
# for x in l:
# 	if x in d:
# 		d[x] += 1
# 	else:
# 		d[x] = 1
# for key, value in d.items():
# 	print(key, value)


# Task 3
def f(x)

d = {}
x = 0
n = int(input())
while n > 0:
    x = int(input())
    if x not in d:
        d[x] = f(x)
        print(d[x])
    else:
        print(d[x])
    n -= 1