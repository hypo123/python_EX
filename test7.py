class Teacher(object):
	__slots__ = ('high' , 'age')
	pass


t1 = Teacher()
t1.age = 100
# t1.sex = 1
t1.high = 150
print('age :',t1.age)
# print('sex :',t1.sex)
print('high:',t1.high)
