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

if (myList[2]):
	print("The third element in myList has a true boolean value!")

print(type(myList))

newList = [[1,2,3],[4,5,6],[7,8,9]]
print(newList[0][2])

print(newList[:2])
