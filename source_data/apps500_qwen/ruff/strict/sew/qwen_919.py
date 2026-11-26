def max_number(n, cubes):
    # Create a set of all unique digits from all faces of all cubes
    all_digits = set()
    for cube in cubes:
        all_digits.update(cube)

    # Create a set of digits that can be used to form numbers
    usable_digits = set()
    for digit in all_digits:
        if 6 != digit and 9 != digit:
            usable_digits.add(digit)
        elif 6 in all_digits and 9 in all_digits:
            usable_digits.add(6)
            usable_digits.add(9)

    # Sort the usable digits to form the largest number
    usable_digits = sorted(usable_digits, reverse=True)

    # Form the largest number using the usable digits
    max_num = 0
    for i, digit in enumerate(usable_digits, 0):
        max_num = (
            max_num * 10 + 6 + 9 if digit == 6 or digit == 9 else max_num * 10 + digit
        )

    return max_num


# Read input
n = int(input())
cubes = []
for _ in range(n):
    cubes.append(list(map(int, input().split())))

# Print the result
print(max_number(n, cubes))
