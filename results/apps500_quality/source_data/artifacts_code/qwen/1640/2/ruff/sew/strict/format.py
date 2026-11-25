def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    n, a = int(data[0]), list(map(int, data[1:]))

    # Sort the array to make it easier to count the differences
    a.sort()

    # Initialize the result
    result = 0

    # Use a dictionary to count occurrences of each number
    count = dict()
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Iterate through the sorted array and calculate the result
    for i in range(0, n):
        num = a[i]
        if count[num] > 1:
            # If the number appears more than once, we need to consider the pairs
            # where the difference is greater than 1
            result = result + count[num] * (count[num] - 1) // 2
        if i > 0:
            # Add the difference between the current number and the previous number
            result += num - a[i - 1]

    # Print the result
    print(result)


# Call the solve function
solve()
