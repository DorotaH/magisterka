from sys import stdin

input = stdin.read
data = input().split()

s, t = data[0], data[1]

# Check if t is a substring of s
if t not in s:
    # If t is a substring of s, the maximum value of i is the number of times t appears in s
    print(-1)
else:
    # If t is not a substring of s, the number of non-negative integers i is infinite
    max_i = s.count(t)
    print(max_i)
