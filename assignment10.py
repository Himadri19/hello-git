Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #1
>>> class Animal():
	'''
	This the base class that showcase the features of class animal
	'''
	legs = 4
	eyes = 2
	ears = 2
	def animal_attribute(self):
		'''
	        This a method of class Animal
	        '''
		print("animal has %d legs"%self.legs)
		print("animal has %d eyes"%self.eyes)
		print("animal has %d ears"%self.ears)

		
>>> class tiger(Animal):
	'''
        This will access the base class Animal
        '''
	typ = "carnivorous"
	def access(self):
		print("this animal is %d "%self.typ)
		print("This animal has %d legs"%self.legs)
		print("This animal has %d ears"%self.ears)
		print("This animal has %d eyes"%self.eyes)

		
>>> obj = Animal()
>>> obj.animal_attribute()
animal has 4 legs
animal has 2 eyes
animal has 2 ears
>>> obj1=tiger()
>>> obj1.animal_attribute()
animal has 4 legs
animal has 2 eyes
animal has 2 ears
>>> #2
>>> class A():
	def f(self):
		return self.g()
	def g(self):
		return 'A'

	
>>> class B(A):
	def g(self):
		return 'B'

	
>>> a = A()
>>> b = B()
>>> print(a.f(),b.f())
A B
>>> #3
>>> class cop():
	'''
        This class will show the details of class cop
        '''
	def __init__(self,name,age,workexp,des):
		self.name=name
		self.age=age
		self.workexp=workexp
		self.des=des
	def add_details(self):
		self.name=input("enter name")
		self.age=input("enter age")
		self.workexp=input("enter workexp")
		self.des=input("enter the destination")
	def display_details(self):
		print("the name is " + str(self.name))
		print("the age is " +str(self.age))
		print("the workexp is " +str(self.workexp))
		print("the des is " +str(self.des))
	def update_details(self):
		self.name=input("enter name")
		self.age=input("enter age")
		self.workexp=input("enter workexp")
		self.des=input("enter the destination")

		
>>> class mission(cop):
	def add_mission_details(self):
		self.country = country
		self.file = file

		
>>> obj = cop('name','age','work experience','destination')
>>> obj.add_details()
enter namehimadri
enter age21
enter workexp2
enter the destinationagent
>>> obj.display_details()
the name is himadri
the age is 21
the workexp is 2
the des is agent
>>> obj.update_details()
enter nameishita
enter age23
enter workexp4
enter the destinationmanager
>>> obj.display_details()
the name is ishita
the age is 23
the workexp is 4
the des is manager
>>> #4
>>> class shape():
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		print("area is" +str(self.length*self.breadth))

		
>>> class Reactangle(shape):
	'''
        inherit class shape
        '''
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth

		
>>> class Square(shape):
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth

		
>>> rect1 = Reactangle(int(input("enter length")),int(input("enter breadth")))
enter length4
enter breadth2
>>> rect1.area()
area is8
>>> sq1 = square(int(input("enter length")),int(input("enter breadth")))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    sq1 = square(int(input("enter length")),int(input("enter breadth")))
NameError: name 'square' is not defined
>>> sq1 = Square(int(input("enter length")),int(input("enter breadth")))
enter length2
enter breadth2
>>> sq1.area()
area is4
>>> 
