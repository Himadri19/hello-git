Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = input("enter elements: ")
enter elements: [1,4,"ishita","himadri",["anushka",1997]]
>>> a = list(a.split(" "))
>>> a
['[1,4,"ishita","himadri",["anushka",1997]]']
>>> a.append(["google","apple","facebook","microsoft","tesla"])
>>> a
['[1,4,"ishita","himadri",["anushka",1997]]', ['google', 'apple', 'facebook', 'microsoft', 'tesla']]
>>> a.count('himadri')
0
>>> b = [27,75,0,8,3,2,8]
>>> b.sort()
>>> b
[0, 2, 3, 8, 8, 27, 75]
>>> A = [29,87,0,4,27]
>>> B = [46,78,55,2]
>>> C = A + B
>>> C
[29, 87, 0, 4, 27, 46, 78, 55, 2]
>>> C.sort()
>>> C
[0, 2, 4, 27, 29, 46, 55, 78, 87]
>>> stack = ['hello','my','name','is']
>>> stack.append('himadri')
>>> stack
['hello', 'my', 'name', 'is', 'himadri']
>>> stack.pop()
'himadri'
>>> 
