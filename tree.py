#!/usr/bin/env python3

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert new data into the tree
    def insert(self, new_data):
        # insert on right side...
        if (new_data > self.data):
            if (self.right == None):
                self.right = Tree(new_data)
            else:
                self.right.insert(new_data)
        # insert on left side...
        else:
            if (self.left == None):
                self.left = Tree(new_data)
            else:
                self.left.insert(new_data)
            
    def search(self, to_search):
        if (self.data == to_search):
            return True

        # Check if belongs in left side...
        if (self.data > to_search and self.left != None):
            return self.left.search(to_search)
        # Check right side exists...
        elif (self.right != None):
            return self.right.search(to_search)
        return False

    def show(self):
        if (self.left != None):
            self.left.show()
        print(str(self.data))
        if (self.right != None):
            self.right.show()

    def remove(self, data):
        pass

tree = Tree(0)
tree.insert(1)
tree.insert(-1)
print(tree.search(1))
print(tree.search(2))
tree.show()
