#!/usr/bin/python3

# Strings are, essentially, lists of single characters
myString = "Hello"

# You access specific characters of a string the same as a list
print(myString[2])

# Strings are however, immutable. They cannot be extended or changed.
# This causes an error! We're trying to change the second character in our string...
myString[1] = 'a'
