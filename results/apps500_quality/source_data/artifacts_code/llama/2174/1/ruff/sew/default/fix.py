
n = int(input())
a = list(map(int, input().split()))

left = 0
right = n - 1
moves = 0

for i in range(n):
    moves += abs(a[i] - (1 + i))
    if  a[i] < 1 + i:
        left = left + 1
    if  a[i] > 1 + i:
        right = right + 1

print(moves + left + right)