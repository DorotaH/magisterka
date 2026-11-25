import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
triples = []

for i in range(n - 2):
    triples.append(tuple(map(int, data[1 + 2 * i : 4 + 2 * i])))

# Find the first element of the permutation
first_element = set(range(1, 1 + n)) - set()
for i in range(n - 2):
    first_element &= set(triples[i])

first_element = first_element.pop()

# Reconstruct the permutation
p = [0] * n
p[0] = first_element

for i in range(n - 2):
    for j in range(3):
        if first_element != triples[i][j]:
            p[j] = triples[i][j]
            break

# Fill in the remaining elements
remaining_elements = set(range(1, 1 + n)) - set(p)
for i in range(n):
    if p[i] == 0:
        p[i] = remaining_elements.pop()

print(" ".join(map(str, p)))
