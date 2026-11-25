def lucky_number_index(n):
    """
    Given a lucky number n, returns its 1-based index in the sorted list of all lucky numbers.
    A lucky number is a positive integer whose decimal representation contains only the digits 4 and 7.
    """
    lucky_numbers = []
    i = 1
    while True:
        # Convert i to string to check its digits
        str_i = str(i)

        # Check if all digits are 4 or 7
        if all(d in '47' for d in str_i):
            lucky_numbers.append(i)

        # If we found the given number, return its index
        if str_i == str(n):
            return lucky_numbers.index(i) + 1

        # If we haven't found the number yet, increment i
        i += 1


# Read input from standard input
n = int(input())

# Print the result
print(lucky_number_index(n))
