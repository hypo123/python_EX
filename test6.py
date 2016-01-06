class Animal(object):
	def run(self):
		print('Animal is running...')


class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

class Apple(object):
	pass

a = Apple()			#可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
a.name = 'red apple' #给实例绑定属性
print(a.name)

def set_age(self , age):
	self.age = age

from types import MethodType
a.set_age = MethodType(set_age , a)#给实例绑定一个方法
a.set_age(25)
print(a.age)

a2 = Apple()
#a2.set_age(36)#给实例绑定的方法，对其他实例不起作用

def set_score(self , score):
	self.score = score
def get_score(self):
	return self.score

Apple.set_score = MethodType(set_score, Apple)#给类绑定方法后，所有实例均可用
Apple.get_score = MethodType(get_score, Apple)

a3 = Apple()
a3.set_score(100)
print(a3.get_score())
