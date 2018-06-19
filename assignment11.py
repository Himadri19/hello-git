Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #1
>>> import threading
>>> import time
>>> class MyThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name=name
	def run(self):
		print("starting: " + self.name)
		time.sleep(5)
		print("hi")
		print("exiting:" + self.name)

		
>>> threadob = MyThread(1)
>>> threadob.setName('himu')
>>> threadob.start()
>>> starting: himu
hi
exiting:himu

>>> #3
>>> import threading
>>> import time
>>> class MyThread(threading.Thread):
	def __init__(self,list,name):
		threading.Thread.__init__(self)
		self.list = list
		self.name = name
	def run(self):
		print("starting:" + self.name)
		for i in range(0,5):
			time.sleep(i * 2)
			print(list[i])
			print("exiting" + self.name)

			
>>> list=[2,3,4,5,6]
>>> thread1=MyThread(list,"himu")
>>> thread1.start()
starting:himu
>>> 
2
exitinghimu
3
exitinghimu
4
exitinghimu
5
exitinghimu
6
exitinghimu

>>> #4
>>> import threading
>>> import math
>>> import time
>>> def fact():
	num=int(input("enter number"))
	res = math.factorial(num)
	print("factorial:",res)

	
>>> threading.Thread(target=fact).start()
enter number
>>> 5
factorial: 120
