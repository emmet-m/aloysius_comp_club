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
		node.children = node.children + [addChildren(child, info)]
	return node
