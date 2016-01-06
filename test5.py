class Student(object):
	def __init__(self , name , score):
		self.__name = name
		self.__score =score #实例的变量名如果以__开头，就变成了一个私有变量（private）

	def print_score(self):
		print('%s: %s' %(self.__name, self.__score))
	def get_score(self):
		return self.__score
	def set_score(self , score):#set方法
		self.__score = score

bart = Student('Bart Simpson' , 59)
bart.__score = 99
# bart.__name = 'Linda Simpson'
bart.print_score()
bart.set_score(100)
bart.print_score()

lisa = Student('Lisa Simpson' , 23)
lisa.print_score()
lisa.sex = 1
lisa.high = 165
lisa.age = 25
print('sex  :',lisa.sex)
print('high :',lisa.high)
print('age :',lisa.age)

