d = {'Michael':95,'Bob':75,'Tracy':85}
d['Jack'] = 90
print(d['Michael'])
print(d['Jack'])

def my_abs(x):
	if x > 0:
		return x
	else:
		return -x

print(my_abs(-10))

def my_power(x,n=2):#默认参数
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(my_power(3,3))

def my_calc(*numbers):#可变参数
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print('sum = ',my_calc(1,2,3,4))


