Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Circle():
	def __init__(self,radius):
		self.radius = radius
	def getArea(self):
		print("Area is :"+ str(3.14*self.radius*self.radius))
	def getCircumference(self):
		print("Circumference is :"+str(self.radius*2*3.14))

		
>>> ob=Circle(float(input('enter the radius:')))
enter the radius:2
>>> ob.getArea()
Area is :12.56
>>> ob.getCircumference()
Circumference is :12.56
>>> #2
>>> class Student():
	def __init__(self,name,roll):
		self.name = name
		self.roll = roll
	def display(self):
		print(self.name)
		print(self.roll)

		
>>> ob = Student(input('enter name of the student :'),input("enter his roll number"))
enter name of the student :himu
enter his roll number17
>>> ob.display()
himu
17
>>> class temperature():
	def convertFahrenheit(self,cel):
		print("temperature in Fahrenheit: "+ str((cel * (9/5))+32))
	def convertCelsius(self,fah):
		print("temperature in celsius: "+ str((fah-32) * (5/9)))

		
>>> obj = temperature()
>>> obj.convertFahrenheit(int(input("enter temp in celsius")))
enter temp in celsius45
temperature in Fahrenheit: 113.0
>>> obj.convertCelsius(int(input("enter temp in fah")))
enter temp in fah113
temperature in celsius: 45.0
>>> class MovieDetails():
	def __init__(self,moviename,artistname,yor,ratings):
		self.moviename = moviename
		self.artistname = artistname
		self.yor = yor
		self.ratings = ratings
	def display(self):
		print("movie name :"+str(self.moviename))
		print("artist name :"+str(self.artistname))
		print("year of release :"+str(self.yor))
		print("ratings :"+str(self.ratings))
	def update(self):
		self.moviename = input("enter updated movie name   :")
		self.artistname = input("enter updated artist name  :")
		self.yor = input("enter updated year of release   :")
		self.ratings = input("enter updated ratings    :")

		
>>> obj = MovieDetails("titanic","leonardo",'1997','5')
>>> obj.display()
movie name :titanic
artist name :leonardo
year of release :1997
ratings :5
>>> obj.update()
enter updated movie name   :lionking
enter updated artist name  :i dont know
enter updated year of release   :2002
enter updated ratings    :5
>>> obj.display()
movie name :lionking
artist name :i dont know
year of release :2002
ratings :5
>>> #5
>>> class expenditure():
	def __init__(self,exp,sav):
		self.exp = exp
		self.sav = sav
	def display(self):
		print("expenditure is:"+str(self.exp))
		print("saving is "+str(self.sav))
	def totalsalary(self):
		expenditure.totalsalary = self.exp + self.sav
	def display(self):
		print("total salary is :"+str(self.totalsalary))

		
>>> ob = expenditure(input("enter expenditure"),input("enter savings"))
enter expenditure2500
enter savings500
>>> ob.totalsalary()
>>> ob.display()
total salary is :2500500
>>> 
