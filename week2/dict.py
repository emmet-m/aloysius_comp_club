#!/usr/bin/python3

dictionary = {}

dictionary["Dennis"] = "Please"
dictionary["True"] = True
dictionary["Integer"] = 5

for key in dictionary.keys():
	print(str(dictionary[key]))

print(type(dictionary))
