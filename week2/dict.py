#!/usr/bin/python3

# Create an empty dictionary like this
dictionary = {}

# Reset the old dictionary to a new one with starting values
dictionary = {"favNumber" : 5, "badNumber" : 13}

dictionary["Dennis"] = "Please"
dictionary["True"] = True
dictionary["Integer"] = -5

# Iterate over the keys in the dictionary.
# This loop reads like this:
# "for every value in dictionary.keys(), store a value in 'key', and run the loop body"
for key in dictionary.keys():
	# Print the value for the given key as a string
	print(str(dictionary[key]))

# Print the type of dictionary
print(type(dictionary))
