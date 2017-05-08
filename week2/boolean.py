#!/usr/bin/python3

# Set two variables, with a true and false value
t = True
f = False

# t is true, so the if statement gets executed!
if (t):
	print("True!")

# f is false, so this statement doesn't
if (f):
	print("This will never be printed!")

# not false = true, so this statement gets executed
if (not f):
	print("Not false?")

# The type of a true or false value is 'bool', short for boolean
print(type(f))

# the type of our variable t is bool, so this statement is executed.
if type(t) is bool:
	print("f is a boolean!")
