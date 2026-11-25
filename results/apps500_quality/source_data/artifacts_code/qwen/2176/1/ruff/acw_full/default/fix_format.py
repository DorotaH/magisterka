from collections import defaultdict

MOD = 998244353


def count_good_permutations(n, pairs):
    # Separate pairs into two lists based on their first and second elements
    first_elements = [pair[0] for pair in pairs]
    second_elements = [pair[1] for pair in pairs]

    # Count occurrences of each element in the first and second lists
    first_count = defaultdict(int)
    second_count = defaultdict(int)
    for a, b in pairs:
        first_count[a] += 1
        second_count[b] += 1

    # Calculate the number of good permutations
    good_permutations = 1
    for i in range(1, 1 + n):
        good_permutations = (
            good_permutations * (second_count[i] + first_count[i])
        ) % MOD

    return good_permutations


# Read input
n = int(input().strip())
pairs = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Calculate and print the result
print(count_good_permutations(n, pairs))
