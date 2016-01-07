class FirstClass:
	def setdata(self , value):
		self.data = value
	def display(self):
		print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata("King III")
y.setdata(3.14159)

x.display()
y.display()

class SecondClass(FirstClass):
	def  display(self):
		print('Current value = "%s"' %self.data)

z = SecondClass()
z.setdata(42)
z.display()

class ThirdClass(SecondClass):
	def __init__(self , value):
		self.data = value
	def __add__(self , other):
		return ThirdClass(self.data + other)
	def __str__(self):
		return '[ThirdClass: %s]' % self.data
	def mul(self , other):
		self.data *= other

a = ThirdClass('abc') #调用__init__ 
a.display()

print(a) #__str__

b = a + 'xyz' #__add__
b.display()

print(b)

a.mul(3) #mul
print(a)