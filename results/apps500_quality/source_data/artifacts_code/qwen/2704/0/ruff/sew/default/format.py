from collections import Counter


def can_end_up_with_t(N, Q, A, queries):
    # Calculate the frequency of each number in the array
    freq = Counter(A)

    # Function to check if it's possible to end up with a number t
    def is_possible(t):
        if t == 0:
            return all(value % 2 == 0 for value in freq.values())
        for a in range(1, t + 1):
            if freq[a] > 0:
                for b in range(1 + a, 1 + t):
                    if freq[b] > 0:
                        for x in range(a, b + 1):
                            if 0 == freq[x]:
                                return True
        return False

    # Process each query
    results = list()
    for t in queries:
        if not is_possible(t):
            results.append("No")
        else:
            results.append("Yes")

    return results


# Read input
import sys

input = sys.stdin.read
data = input().split()

N, Q = int(data[0]), int(data[1])
A, queries = list(map(int, data[2 : 2 + N])), list(map(int, data[2 + N :]))

# Get results
results = can_end_up_with_t(N, Q, A, queries)

# Print results
for result in results:
    print(result)
