def can_sort_by_handles(n, handles, p):
    # Create a list of tuples (first name, last name, handle index)
    people = [(f, s, i) for i, (f, s) in enumerate(handles)]

    # Sort people by their handle index
    sorted_people = sorted(people, key=lambda x: p[x[2]])

    # Create two lists to store the handles sorted by first name and last name
    first_name_handles = [f for f, s, _ in sorted_people]
    last_name_handles = [s for f, s, _ in sorted_people]

    # Check if the sorted handles match the given permutation for either first name or last name
    if all(first_name_handles[i] < first_name_handles[i + 1] for i in range(n - 1)):
        return "YES"
    if all(last_name_handles[i] < last_name_handles[i + 1] for i in range(n - 1)):
        return "YES"

    return "NO"


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
handles = [(data[2 * i + 1], data[2 * i + 2]) for i in range(n)]
p = [int(data[2 * n + 1 + i]) for i in range(n)]

# Output result
print(can_sort_by_handles(n, handles, p))
