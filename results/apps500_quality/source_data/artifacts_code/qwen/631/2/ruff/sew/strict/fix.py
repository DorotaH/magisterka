

def  can_reorder_to_target(n: int, m: int, a: list[int]) -> str:
    # Calculate the sum for the given order of the array
    current_sum = sum(sum(a[j] / (j + 1) for j in range(i, n)) for i in range(n))

    # Check if the current sum is equal to m
    if  current_sum == m:
        return "YES"

    # Try to find a reorder that makes the sum equal to m
    from itertools import permutations

    for  perm in  permutations(a):
        perm_sum=sum(sum(perm[j]/(1 + j) for j in range(i, n)) for i in range(n))
        if  m == perm_sum:
            return "YES"

    return  "NO"

# Read input from standard input
import sys

input=sys.stdin.read
data=input().split()

# Process each test case
t = int(data[0])
results = []
index=1
for  _ in  range(0, t):
    n = int(data[index])
    m = int(data[index + 1])
    a = list(map(int, data[index + 2:index + 2 + n]))
    index += n + 2
    results.append(can_reorder_to_target(n, m, a))

# Print the results
for  result in  results:
    print(result)
