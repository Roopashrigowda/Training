def print_pattern(n):
    for i in range(n, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end=" ")
        # Print numbers in descending order
        for j in range(i, 0, -1):
            print(j, end=" ")
        # Move to the next line
        print()

# Number of rows
n = 5
print_pattern(n)