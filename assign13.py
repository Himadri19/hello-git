#1
try:
    a=3
    if a<4:
     a=a/(a-3)
except (ZeroDivisionError,IndentationError):
    print("The answer is 0.")
else:
     print(a)
"""indentation error and zerodivisionerror occurred"""

#question 2
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("cannot find element")
    '''range out of range'''

#3
"""try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not"""

"""Name Error:If Python encounters a name that it doesn't recognize,you'll get this error."""

"""
answer 3: raise NameError("Hi there")  # Raise Error
          NameError: Hi there
"""
#4

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

"""answer 4: -5.0
             a/b result in 0
"""
#5
"""Import error: It basically comes when we try to import any module that is not present.If python cannot find the module."""
try:
 import mountain
except ImportError:
  print("This module is not present.")

"""Value error:It is raised when a built-in operation or function receives an argument that has the right type but an appropriate value"""
while True:
    try:
      n=int(input("please,Enter a number:"))
      break
    except ValueError:
      print("You are supposed to enter a number!please try again...")
print("great,you successfully entered a number.")

"""Index error:It is raised whenever attempting to access an index that is outside the bounds of a list"""
try:
     list=[1,2]
     print(list[4])
except IndexError:
   print("This element can not be accessed.")
#6
class AgeTooSmallError(Exception):
    pass

def input_age():
    num = int(input("Enter the age:"))
    return num

age=18
while True:
    try:
        num = input_age()
        if num<age:
            raise AgeTooSmallError
        else:
            print("Age correct...")
            break
    except AgeTooSmallError:
        print("error,Age is too small,enter again...")



