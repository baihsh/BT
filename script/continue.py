#!/usr/bin/python
#Filename: continue.py

while True:
	s = raw_input('ENter something : ')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print 'Input is of sufficient length'
	#Do other kinds of processing here ...
