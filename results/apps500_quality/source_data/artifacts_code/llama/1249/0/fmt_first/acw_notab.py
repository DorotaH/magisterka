from collections import defaultdict
import sys


def read_ints():
    return list(map(int, sys.stdin.readline().split()))


def main():
    m, k, n, s = read_ints()
    a = read_ints()
    b = read_ints()

    # Count occurrences of each type in the weaving schematic
    b_count = defaultdict(int)
    for i in range(s):
        b_count[b[i]] += 1

    # Calculate the number of times the machine cuts the liana
    cuts = (m - 1) // k + 1

    queue = [a[i] for i in range(k)]
    for i in range(k, m):
        queue[i % k] = max(queue[i % k], queue[(i - k) % k])
        queue.append(a[i])

    # Initialize a list to store the types of flowers in the liana
    types = [0] * (5 * 10**5 + 1)

    # Calculate the number of occurrences of each type in the liana
    for i in range(m):
        types[a[i]] += 1

    # Initialize a list to store the result
    result = []

    # Process each workpiece
    for i in range(cuts):
        # If this workpiece fits the schematic, add it to the result
        if all(types[j] >= b_count[j] for j in range(1, 5 * 10**5 + 1)):
            result.append(i)
            break

        # Remove the first flower from the queue
        types[queue.pop(0)] -= 1

        # Add the next k flowers to the queue
        queue.extend(a[i * k + j] for j in range(k))
        # Update the types of flowers in the liana
        for j in range(k):
            types[a[i * k + j]] += 1

    # If no workpiece fits the schematic, print -1
    if not result:
        print(-1)
        return

    # Print the result
    print(len(result))
    print(*[i * k + j + 1 for j in range(k) for i in result])


if __name__ == "__main__":
    main()
