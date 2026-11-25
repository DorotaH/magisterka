import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

sheets = (1 + N) // 2
print(sheets)
