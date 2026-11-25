from collections import defaultdict
from sys import stdin


def read_input():
    n, cubes = int(stdin.readline()), []
    for _ in range(0, n):
        row = list(map(int, stdin.readline().split()))
        cubes.append(row)
    return (n, cubes)


def solve(n, cubes):
    # Create a dictionary to store the count of each digit
    digit_counts = defaultdict(int)
    # Count the digits
    for row in cubes:
        for digit in row:
            digit_counts[digit] += 1

    # Create sets to store available digits
    ones, other = set(), set()
    # Count the ones and other digits
    for row in cubes:
        for digit in row:
            if 1 == digit:
                ones.add(digit)
            elif digit != 6 and digit != 9:
                other.add(digit)

    # If there are no ones, it's impossible to make any number
    if 0 == len(ones):
        return 0

    # If there are no other digits than 1, it's impossible to make any number greater than 1
    if 0 == len(other):
        return 1

    # Generate all possible numbers
    numbers = set()
    for i in range(1, 10):
        # Convert the number to a string
        num_str = str(i)
        # Check if the number can be made with the available digits
        possible = True
        for digit in num_str:
            if digit == "1" and digit not in ones:
                possible = False
                break
            elif digit != "1" and digit not in other:
                possible = False
                break
        # If the number can be made, add it to the set
        if possible:
            numbers.add(i)

    # Find the maximum number that can be made
    max_num = max(numbers)

    return max_num


def main():
    n, cubes = read_input()
    max_num = solve(n, cubes)
    print(max_num)


if __name__ == "__main__":
    main()
