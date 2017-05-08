#!/usr/bin/python3

import sys

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

i = 2

wait = input("Press enter to continue...")

while (True):
	print("\n" + str(i) + " " + str(sys.getsizeof(i)) + "\n")
	i = i*2
