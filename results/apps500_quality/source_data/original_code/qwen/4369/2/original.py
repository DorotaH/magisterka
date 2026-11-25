import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])

sheets = (N + 1) // 2
print(sheets)
