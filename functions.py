Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> r = float(input("enter radius"))
enter radius6
>>> def area(r):
	PI = 3.14
	area = PI*r*r
	return area

>>> print(area(r))
113.03999999999999
>>> #2
>>> def perf():
	sum = 0
	i = 1
	while sum<1000:
		sum+=i
		print(sum)
		i+=1

		
>>> perf()
1
3
6
10
15
21
28
36
45
55
66
78
91
105
120
136
153
171
190
210
231
253
276
300
325
351
378
406
435
465
496
528
561
595
630
666
703
741
780
820
861
903
946
990
1035
>>> #3
>>>  def mul(n,i):
	if i<=10:
		print(str(n) + "*" +str(i)+"="+str(n*i))
		mul(n,i+1)
	else:
		print()
		
SyntaxError: unexpected indent
>>> 
>>> def mul(n,i):
	if i<=10:
		print(str(n) + "*" +str(i)+"="+str(n*i))
		mul(n,i+1)
	else:
		print()

		
>>> mul(12,1)
12*1=12
12*2=24
12*3=36
12*4=48
12*5=60
12*6=72
12*7=84
12*8=96
12*9=108
12*10=120

>>> #4
>>> a = int(input("enter"))
enter2
>>> b =int(input("enter"))
enter2
>>> def power(a,b):
	if b == 1:
		return a
	else:
		return (a*power(a,b-1))
	print(power(a,b))

	
>>> print(power(a,b))
4
>>> #5
>>> num = int(input("enter no"))
enter no5
>>> def fact(n):
	if n==1:
		return 1
	else:
		return(n*fact(n-1))

	
>>> f=fact(num)
>>> dict={num:f}
>>> print(dict)
{5: 120}
>>> 
