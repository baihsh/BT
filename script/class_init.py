#!/usr/bin/python
#Filename:  class_init.py

class Person:
	def __init__(self, name):
		self.myname = name
	def sayHi(self):
		print 'Hello, my name is', self.myname
p = Person('Baihsh')
p.sayHi()

# This short example can also be written as Person('Baihsh').sayHi()
