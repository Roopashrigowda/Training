def print_star_pattern(n):
    for i in range(n):
        # Calculate spaces before and between stars
        if i <= n // 2:
            leading_spaces = i
            middle_spaces = n - 2 * i - 2
        else:
            leading_spaces = n - i - 1
            middle_spaces = 2 * i - n

        # Print leading spaces
        print(" " * leading_spaces, end="")

        # Print first star
        print("*", end="")

        # Print middle spaces if any
        if middle_spaces >= 0:
            print(" " * middle_spaces, end="")

            # Print second star if any
            if middle_spaces >= 0:
                print("*", end="")

        # Move to the next line
        print()

# Number of rows
n = 5
print_star_pattern(n)