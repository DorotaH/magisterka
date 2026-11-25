def find_partition(n, sequence):
    from collections import defaultdict

    # Dictionary to store numbers that can be divided by a given number
    divisors = defaultdict(list)

    # Populate the divisors dictionary
    for num in sequence:
        for i in range(1, num + 1):
            if num % i == 0:
                divisors[i].append(num)

    # Try to form groups
    groups = []
    for i in range(n // 3):
        # Find the smallest number that can be the start of a group
        start = min(divisors)
        if len(divisors[start]) < 2:
            return -1
        a, b = divisors[start].pop(0), divisors[start].pop(0)

        # Find the number that can be the end of the group
        if b not in divisors:
            return -1
        c = divisors[b].pop(0)

        # Add the group to the list
        groups.append((a, b, c))

    return groups


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    sequence = list(map(int, data[1:]))

    result = find_partition(n, sequence)

    if result == -1:
        print(-1)
    else:
        for group in result:
            print(group[0], group[1], group[2])


if __name__ == "__main__":
    main()
