def max_number(n, cubes):
    # Create a set of all unique digits from all faces of all cubes
    all_digits = set()
    for cube in cubes:
        all_digits.update(cube)

    # Create a set of digits that can be used to form numbers
    usable_digits = set()
    for digit in all_digits:
        if digit not in [6, 9]:
            usable_digits.add(digit)
        elif 6 in all_digits and 9 in all_digits:
            usable_digits.add(6)
            usable_digits.add(9)

    # Sort the usable digits to form the largest number
    usable_digits = sorted(usable_digits, reverse=True)

    # Form the largest number using the usable digits
    max_num = 0
    for i, digit in enumerate(usable_digits):
        max_num = 10 * max_num + 6 + 9 if digit in [6, 9] else 10 * max_num + digit
    return max_num


# Read input
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]

# Print the result
print(max_number(n, cubes))
