Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup = (1,2,'ishita','himadri',1.6)
>>> type(tup)
<class 'tuple'>
>>> len(tup)
5
>>> len(tup[3])
7
>>> #question 2
>>> tup2 = (2,3,4,7,99,56)
>>> len(tup2)
6
>>> length = len(tup2)
>>> sorted(tup2)
[2, 3, 4, 7, 56, 99]
>>> print("Largest element is:", tup2[length-1])
Largest element is: 56
>>> print("Smallest element is:", tup2[0])
Smallest element is: 2
>>> #question 3
>>> tup3 = (2,7,1,10)
>>> product = (2*7*1*10)
>>> product
140
>>> #question 4
>>> a = input("enter values in set")
enter values in set1,2,3,4
>>> a = set(a)
>>> type(a)
<class 'set'>
>>> b = input("enter values in set")
enter values in set7,8,3,4
>>> b = set(b)
>>> type(b)
<class 'set'>
>>> c = a - b
>>> print(c)
{'1', '2'}
>>> a==b8
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a==b8
NameError: name 'b8' is not defined
>>> a==b
False
>>> a>=b
False
>>> a<=b
False
>>> d = a & b
>>> d
{',', '3', '4'}
>>> #question 5
>>> dic = {}
>>> for i in range(10):
	key = input()
	value = int(input())
	dic[key] = value

	
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
10
10
>>> print(dic)
{'4': 4, '3': 3, '2': 2, '9': 9, '1': 1, '8': 8, '6': 6, '7': 7, '5': 5, '10': 10}
>>> 
