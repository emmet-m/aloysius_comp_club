#!/usr/bin/python3

# We can set variables to float (decimal) values
half = 0.5
# 0.5 times 5 is 2.5
half = half * 5

# prints 2.5
print(half)

# Make a new float variable
root = 0.0

# iterate over the range 0-100 (i.e. 100 times) and add 0.1 to root each time
for i in range(0,100):
	root += 0.1

# This comes out as not 10. What? Clearly 100*0.1 is 10....
# This is because rounding error deep in the way computers work.
print(root)
# However, we can perform the actual computation and get the correct result like so.
print(0.1*100)

# The type of root is a float!
print(type(root))
