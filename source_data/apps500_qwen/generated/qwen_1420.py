from sys import stdin
input = stdin.read
data = input().split()

s = data[0]
t = data[1]

# Check if t is a substring of s
if t in s:
    # If t is a substring of s, the maximum value of i is the number of times t appears in s
    max_i = s.count(t)
    print(max_i)
else:
    # If t is not a substring of s, the number of non-negative integers i is infinite
    print(-1)
