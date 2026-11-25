def find_partition(n, sequence):
    from collections import defaultdict
    
    # Dictionary to store numbers based on their divisibility
    divisors = defaultdict(list)
    for num in sequence:
        divisors[num].append(num)
    
    # Try to form groups of three (a, b, c) where a < b < c and a divides b, b divides c
    groups = []
    for a in range(1, 8):
        for b in range(a + 1, 8):
            for c in range(b + 1, 8):
                if b % a == 0 and c % b == 0:
                    if a in divisors and b in divisors and c in divisors:
                        groups.append((a, b, c))
                        divisors[a].remove(a)
                        divisors[b].remove(b)
                        divisors[c].remove(c)
    
    # Check if we have used all elements
    if len(groups) * 3 == n:
        return groups
    else:
        return -1

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
sequence = list(map(int, data[1:]))

# Find and print the result
result = find_partition(n, sequence)
if result == -1:
    print(-1)
else:
    for group in result:
        print(group[0], group[1], group[2])
