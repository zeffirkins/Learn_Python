# import os.path
# import struct
#
# with open('C:\\Users\\Iurii\\pyth\\read.txt', 'r') as inf:
# 	s1 = inf.readline().strip() # strip - убрать все служебные символы из строки
# 	s2 = inf.readline().strip()
# print(s1, s2)
# # os.path.join('.', 'dirname', 'filename.txt') # правильно составляет путь в не зависимости от системы

# with open('C:\\Users\\Iurii\\read.txt') as inf:
# 	for line in inf:
# 		line = line.strip()
# 		print(line)

# ЗАПИСЬ В ФАЙЛ
# with open('C:\\Users\\Iurii\\pyth\\write.txt', 'w') as ouf:
# 	ouf.write('Serafima\n') # \n для перехода на следующую строку
# 	ouf.write(str(14))  # для записи чисел х нужно привести к строке
#
# with open('C:\\Users\\Iurii\\pyth\\write.txt.') as inf:
# 	s3 = inf.readline().strip() # strip - убрать все служебные символы из строки
# 	s4 = inf.readline().strip()
# print(s3, s4)

# TASK 1 Decoding file

with open('C:\\Users\\Iurii\\pyth\\read.txt.') as inf:
	s = inf.readline().strip()
print(s)
num = 0
symbol = ''
ouf = open ('C:\\Users\\Iurii\\pyth\\write.txt', 'w')
for x in s:
	num = 0
	if x.isdigit():
		num = x
		else:
		symbol = x
ouf.close()

with open('C:\\Users\\Iurii\\pyth\\write.txt.') as inf:
	t = inf.readline().strip()
print(t)