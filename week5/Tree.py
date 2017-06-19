import random

class Tree(object):
	def __init__(self, data):
		self.data = data
		self.children = []

	def getChildren():
		return this.children

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
		if (child == ''):
			break
		node.children = node.children + [addChildren(child, info)]
	return node

def treeGen(size):
	data = {}
	i = 1
	curr = 2
	while i <= size:
		# Have we used up all existing nodes?
		if (size - curr < 1):
			# Initialise the untouched nodes
			while i <= size:
				data[str(i)] = []
				i += 1
			break

		#Pick random amount of children to add, starting at the current latest
		if (size - curr > (size*5)/100):
			# Accounting for small trees
			if (size < 40):
				n = random.randint(1, 3)
			else:
				n = random.randint(1, int((size*5)/100))
		else:
			n = random.randint(1, size - curr)

		toAdd = range(curr, curr + n + 1)
		curr = curr + n

		# Add them
		data[str(i)] = []
		for j in toAdd:
			data[str(i)] = data[str(i)] + [str(j)]

		# Move along
		i = i + 1

	# Now format the data
	toWrite = ""

	keys = [int(x) for x in data.keys()]

	for key in sorted(keys):
		#Add node and marker
		toWrite += (str(key) + ":")
		#Add children following
		for child in data[str(key)]:
			toWrite += child + " "
		# Move to next line
		toWrite += "\n"

	return toWrite
