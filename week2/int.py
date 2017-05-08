#!/usr/bin/python3

import sys

# Integers are positive or negative whole numbers
i = 2

# addition
i = i + 2
print(i)
# subtraction
i = i - 2
print(i)
# multiplication
i = i * 2
print(i)
# division
i = i / 2
print(i)
# Squaring
i = i ** 2
print(i)

# Reset our integer...
i = 2

# Be prepared for the next bit!
input("Press enter to continue...")

# Loop forever.... Press ctrl + c to interrupt a program!
while (True):
	# Print a new line, plus our current number, then it's size in bytes (yes, it's bytes, I googled!).
	print("\n" + str(i) + " " + str(sys.getsizeof(i)) + "\n")
	# Times our number by 2.
	i = i*2
