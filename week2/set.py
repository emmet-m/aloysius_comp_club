#!/usr/bin/python3

# Making a new set
x = set(["a", "b", "c"])
y = set(["b", "c", "d"])

# Doing difference between sets
print(x.difference(y))

# Take the difference between two sets....
z = y - x # y take away the common elements from x only leaves 'd'
print(z)
z = x - y # x take away the common elements from y only leaves 'a'
print(z)


# Intersection gives common elements of sets
z = x.intersection(y) # 'b' and 'c' are common in both sets
print(z)

# A subset is a set that is contained in another set. A superset is the opposite
print(z.issubset(x)) # True, everything in z is in x
print(x.issubset(y)) # False, everything in x is NOT in y
print(x.issuperset(z)) # True, x contains everyting in z, and more # True, x contains everyting in z, and more!!

print(z.pop()) # Picks a random element from the set, removes it, and returns it.
