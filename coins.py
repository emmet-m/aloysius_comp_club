#!/usr/bin/env python3

# Solving the famous 'Change' problem with dynamic programming
# To find the least amount of coins needed from given values to make a certain amount of money
# Both iterative and recursive solutions below

# Iterative solution
def iterate(values, coins, M):
    # We want to iterate over all the cell values, including M
    for i in range(1,M+1):
        # Skip the first case
        # Worst case will always be <= M, so we can start our 'best' here
        best = M
        # Check each coin value
        for coin in coins:
            # If our coin value is too large to build apon, we skip
            if i - coin < 0:
                continue
            # If the current coin + index combination is better than our previous best, use that instead
            if grid[i - coin] + 1 < best:
                best = grid[i - coin] + 1
        # Set the current value to be the best value we found
        values[i] = best

# Recursive solution
def recurse(values, index, coins, M):
    # Create a best
    best = M 
    # Iterate over coins
    for coin in coins:
        # Skip invalid coins
        if index - coin < 0:
            continue
        # If a subproblem is unsolved, solve it before we use it
        if values[index - coin] == -1:
            recurse(values, index - coin, coins, M)
                
        # If the current coin + previous value is better than best, we replace best
        if best > values[index - coin] + 1:
            best = values[index - coin] + 1
    # set the value of the previous best
    values[index] = best

# Collect the values we want to compute with
coins = input("Enter the coin values: ").split(" ")
coins = [int(x) for x in coins]
M = int(input("Enter a value: "))

# Make a grid of size M + 1 of negative values, set the first subproblem to 0
grid = [-1]*(M+1)
grid[0] = 0

# Recursively solve, top-down
recurse(grid, M, coins, M)

# Reset the grid
grid = [-1]*(M+1)
grid[0] = 0

# Iteratively solve, bottom up
iterate(grid, coins, M)

print("The best amount of coins is: " + str(grid[M]))
