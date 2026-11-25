from collections import defaultdict


def find_min_kth_statistic(n, s, m, k, a, segments):
    # Create a dictionary to store the indices of each element in the list
    index_map = defaultdict(list)
    for i in range(n):
        index_map[a[i]].append(i)

    # Create a list of sets to store the indices of elements covered by each segment
    segment_indices = [set() for _ in range(s)]
    for j in range(s):
        l, r = segments[j]
        for i in range(l - 1, r):
            segment_indices[j].add(i)

    # Create a list of tuples to store the elements covered by the segments
    covered_elements = []
    for i in range(s):
        covered_elements.extend(
            a[i] for j in index_map[a[i]] if j in segment_indices[i]
        )
    # Sort the covered elements
    covered_elements.sort()

    # Check if it's possible to select at least k elements
    return -1 if len(covered_elements) < k else covered_elements[k - 1]


# Read input
n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(s)]

# Find the minimum k-th statistic
result = find_min_kth_statistic(n, s, m, k, a, segments)

# Print the result
print(result)
