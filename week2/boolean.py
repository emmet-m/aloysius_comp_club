#!/usr/bin/python3

t = True
f = False

if (t):
	print("True!")

if (f):
	print("This will never be printed!")

if (not f):
	print("Not false?")

print(type(f))

if type(f) is bool:
	print("f is a boolean!")
