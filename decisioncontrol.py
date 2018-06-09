Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> year = int(input("enter year"))
enter year2000
>>> if (year%4==0):
   if (year%100==0):
       if (year%400==0):
           print("leap year")
       else:
           print("not a leap year")
   else:
       print("leap year")
else:
   print("not a leap year")

   
leap year
>>> #question 2
>>> length = int(input("enter length"))
enter length30
>>> breadth = int(input("enter breadth"))
enter breadth20
>>> if (length == breadth):
	print("dimensions are of square")
else:
	print("dimensions are of rectangle")

	
dimensions are of rectangle
>>> #question 3
>>> first = int(input("enter age"))
enter age30
>>> second = int(input("enter age"))
enter age60
>>> third = int(input("enter age"))
enter age80
>>> if (first>=second and first>=third):
	print("first oldest")
elif (second>=first and second>=third):
	print("second oldest")
elif (third>=first and third>=second):
	print("third oldest")

	
third oldest
>>> if(first<=second and first<=third):
	print("first youngest")
elif  (second<=first and second<=third):
	print("second youngest")
elif (third<=first and third<=second):
	print("third youngest")

first youngest
>>> #question4
>>> points = int(input("enter points"))
enter points152
>>> if (points<=50):
	print("sorry!no priz this time")
elif (points>=51 and points<=150):
	print("congratulations!you won wooden dog")
elif (points>=151 and points<=180):
	print("congratulations!you won book")
elif (points>=181 and points<=200):
	print("congratulations!you won chocolate")
else:
	print("points exceeded")

	
congratulations!you won book
>>> #question 5
>>> quantity = int(input("enter quantity"))
enter quantity50
>>> cost = 100*quatity
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cost = 100*quatity
NameError: name 'quatity' is not defined
>>> cost = 100*quantity
>>> if (cost>1000)
SyntaxError: invalid syntax
>>> if (cost>1000):
	print((cost*90/100))
else:
	print(cost)

	
4500.0
>>> 
