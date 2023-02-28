#			Функции
#	начинаются с def foo(arguments)
#	если количество аргументов произвольноето используется * (*arguments)
#	могут не возвращать ничего
#	могут иметь значения аргументов по умолчанию(step = 1)
#	можно создавать и использовать локальные переменные внутри функции
#
#



# def my_range(start, stop, step = 1): #функция может содержать значения по умолчанию
# 	res = []
# 	if step > 0:
# 		x = start
# 		while x < stop:
# 			res += [x]
# 			x += step
# 	elif step < 0:
# 		x = start
# 		while x > stop:
# 			res += [x]
# 			x += step
# 	return res
#
# print(my_range(2, 5))
# print(my_range(2, 15, 3))
# print(my_range(15, 2, -3))



# b = 0
# def init_values(b):
# 	b = 100
# 	return b
#
# init_values(b)
# print(b)


# def f (x):
# 	ans = 0
# 	if x <= - 2:
# 		ans = 1 - ((x + 2)**2)
# 	elif -2 < x <= 2:
# 		ans = -1 * (x / 2)
# 	else:
# 		ans = ((x - 2)**2) + 1
# 	return ans
#
# print(f(1))


def modify_list(l):
	new_l = []
	for i in l:
		if i % 2 == 0:
			new_l.append(i // 2)
	del l[:]
	l[:] = new_l



	# for i in l:
	# 	if i % 2 != 0:
	# 		l.remove(i)
	# for i in range(len(l)):
	# 	l[i] = l[i] // 2
	#
	# for i in l:
	# 	if i == 0:
	# 		l.remove(i)

lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 1, 4, 4]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
#lst = [10, 5, 8, 3]
#modify_list(lst)
#print(lst)               # [5, 4]