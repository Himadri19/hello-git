Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = []
>>> for i in range (10):
	val = input("enter")
	num.append(val)

enter1
enter2
enter3
enter4
enter5
enter6
enter7
enter8
enter9
enter10
>>> print(num)
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> #2
>>> c = 0
>>> while(c!=1):
	print("inf.loop")

	
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
inf.loop
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    print("inf.loop")
  File "C:\Users\Himadri\AppData\Local\Programs\Python\Python35\lib\idlelib\PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> #3
>>> ls = []
>>> x = int(input("enter size"))
enter size5
>>> for i in range(x):
	val = input("enter")
	ls.append(i)

	
enter1
enter2
enter3
enter4
enter5
>>> ls2 = []
>>> for i in range(x):
	ls2.append(ls[i]*ls[i])

	
>>> print(ls2)
[0, 1, 4, 9, 16]
>>> mylist = [400,'ishita',99,'himadri',0.001,'roar']
>>> myInt = []
>>> myFlt = []
>>> myStr = []
>>> for x in mylist:
	if isinstance(x,int):
		myInt.append(x)
	if isinstance(x,str):
		myStr.append(x)
	if isinstance(x,float):
		myFlt.append(x)

		
>>> print(myInt)
[400, 99]
>>> print(IntFlt)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(IntFlt)
NameError: name 'IntFlt' is not defined
>>> print(myFlt)
[0.001]
>>> print(myStr)
['ishita', 'himadri', 'roar']
>>> #5
>>> even = []
>>> odd = []
>>> for x in range(1,101):
	if x%2 == 0:
		even.append(x)
	else:
		odd.append(x)

		
>>> print(even)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> print(odd)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> #7
>>> dic = {}
>>> i = len(dic.items())
>>> for i in range(3):
	key = input()
	value = int(input())
	dic[key] = value

	


Traceback (most recent call last):
  File "<pyshell#50>", line 3, in <module>
    value = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> c = 0
>>> while c < i:
	k,v =list(dic.items())[c]
	print(k,v)
	c+=1

	
>>> dic = {}
>>> i = len(dic.items())
>>> for i in range(3):
	key = input()
	value = int(input())
	dic[key] = value

	


Traceback (most recent call last):
  File "<pyshell#60>", line 3, in <module>
    value = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> 
