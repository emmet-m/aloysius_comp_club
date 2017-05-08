#!/usr/bin/python3

#Create an empty list
myList = []

#Add something
myList.append(1)
myList.append("Hello")
myList.append(True)

#Display your list
print(myList)

#Print a specific element of a list
print(myList[0])

# True is stored in the third slot of our list, so this becomes if(True)
if (myList[2]):
	print("The third element in myList has a true boolean value!")

# Our list is of course, of type list
print(type(myList))

# You can have lists inside lists! This is essentially a 'grid'. 
newList = [[1,2,3],[4,5,6],[7,8,9]]
# Access nested lists like this
print(newList[0][2])

# The : here specifies a range. This gives us the first trough to third element
print(newList[0:2])

# Leaving sections of the range blank defaults to the end/start 
# From the start until the third element
print(newList[:2])
# From the first until the last element
print(newList[0:])
# This gives us everything in the list
print(newList[:])

# You can skip over a list in jumps of a certain size. 
# Here, we get all elements in the range 0 to 10, grabbing only every second element
anotherList = [0,1,2,3,4,5,6,7,8,9,10]
print(anotherList[0:11:2])
