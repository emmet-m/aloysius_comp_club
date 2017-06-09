#!/usr/bin/env python3.5

# Include our tree library
from Tree import *

# This is your search function to fill in!
def dfs(tree, key):
	#Get rid of this line to execute your function
	pass

# This opens and encodes a tree file. You can use any of the tree files you find!
tree = parseTreeInput("tree1.txt")

# These are all the children encoded in tree. Each of them has their own children, etc.
print(tree.children)
# This is the information stored in the node. In our case, its just a number
print(tree.data)

# Test your searching with some examples below!
