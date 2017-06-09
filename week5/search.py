#!/usr/bin/env python3.5
import re
from Tree import Tree

#
# Ignore these next two functions :^) We'll go over them in class.
#
def parseTreeInput(fileName):
	f = open(fileName, 'r')
	lines = f.readlines()
	info = {}
	for line in lines:
		line = line.rstrip()
		parent = Tree(line.split(":")[0])
		children = line.split(":")[1].split(" ")
		dat = [parent] + children
		info[line.split(":")[0]] = dat

	# Done
	addChildren('1', info)
	
	# return the root
	return info["1"][0]

def addChildren(nodeId, info):
	if nodeId == '':
		return
	dat = info[nodeId]
	node = dat[0]
	children = dat[1:]
	for child in children:
		node.children = node.children + [addChildren(child, info)]
	return node
#
# Everything that interests you is below here!
#

# This is your search function to fill in
# You can get info on stacks here: https://docs.python.org/3.5/tutorial/datastructures.html#using-lists-as-stacks

def depthFirstSearch(tree, key):
	#Get rid of this line to execute your function
	pass

#
tree = parseTreeInput("tree1.txt")
# Test your searching below
