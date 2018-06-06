Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #question no 1
>>> print('hello everyone')
hello everyone
>>> #question no 2
>>> print("acad"+"view")
acadview
>>> x = input('enter value of x=')
enter value of x=5
>>> print(x)
5
>>> y = input('enter value of y=')
enter value of y=6
>>> print(y)
6
>>> z = input('enter value of z=')
enter value of z=7
>>> print(z)
7
>>> #question no 4
>>> print("let's get started")
let's get started
>>> s="Acadeview"
>>> course="python"
>>> fees=5000
>>> print('%s %s %d' % (s,course,fees))
Acadeview python 5000
>>> name="Tony Stark"
>>> salary=1000000
>>> print('%s,%d')%(name,salary)
%s,%d
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('%s,%d')%(name,salary)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> print('%s,%d'%(name,salary))
Tony Stark,1000000
>>> 
