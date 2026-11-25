from collections import defaultdict

def min_changes_to_distinct_substrings(s):
    n = len(s)
    count = defaultdict(int)
    changes = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if count[substring] > 0:
                changes += 1
                s = s[:i] + chr(ord(s[i]) + 1) + s[i+1:]
                count = defaultdict(int)
                for k in range(n):
                    for l in range(k + 1, n + 1):
                        count[s[k:l]] += 1
                break
            count[substring] += 1
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if count[substring] > 1:
                return -1
    
    return changes

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
s = data[1]

# Output the result
print(min_changes_to_distinct_substrings(s))
