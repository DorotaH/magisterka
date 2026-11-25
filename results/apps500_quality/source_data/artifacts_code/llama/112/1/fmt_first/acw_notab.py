from collections import defaultdict
from sys import stdin


def read_input():
    n = int(stdin.readline())
    cubes = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        cubes.append(row)
    return n, cubes


def solve(n, cubes):
    # Create a dictionary to store the count of each digit
    digit_counts = defaultdict(int)
    # Count the digits
    for row in cubes:
        for digit in row:
            digit_counts[digit] += 1

    # Create sets to store available digits
    ones = set()
    other = set()
    # Count the ones and other digits
    for row in cubes:
        for digit in row:
            if digit == 1:
                ones.add(digit)
            elif digit not in [6, 9]:
                other.add(digit)

    # If there are no ones, it's impossible to make any number
    if not ones:
        return 0

    # If there are no other digits than 1, it's impossible to make any number greater than 1
    if not other:
        return 1

    # Generate all possible numbers
    numbers = set()
    for i in range(1, 10):
        # Convert the number to a string
        num_str = str(i)
        possible = not any(
            digit == "1"
            and digit not in ones
            or digit != "1"
            and digit not in other
            for digit in num_str
        )
        # If the number can be made, add it to the set
        if possible:
            numbers.add(i)

    return max(numbers)


def main():
    n, cubes = read_input()
    max_num = solve(n, cubes)
    print(max_num)


if __name__ == "__main__":
    main()
