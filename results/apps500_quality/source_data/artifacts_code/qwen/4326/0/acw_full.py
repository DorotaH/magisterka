import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])

groups_of_three_or_more = N // 3
print(groups_of_three_or_more)
