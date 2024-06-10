# Number of rows and columns
n = 5

# Iterate through each row
for i in range(n):
    # Iterate through each column in the row
    for j in range(n):
        # Print star without newline at the end
        print('*', end=' ')
    # Print newline at the end of the row
    print()