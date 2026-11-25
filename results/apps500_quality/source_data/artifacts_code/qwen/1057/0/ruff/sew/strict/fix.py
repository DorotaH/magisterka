def count_ways_to_remove_substring(s):
    MOD=998_244_353
    n, count = len(s), [0] * 26
    for  char in  s:
        count[ord(char) - ord('a')] += 1

    total_ways=0
    for  char in  s:
        total_ways += count[ord(char) - ord('a')] - 1
        total_ways %= MOD

    return total_ways

# Read input
import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
s = data[1]

# Calculate and print the result
result = count_ways_to_remove_substring(s)
print(result)
