n = int(input())
a = list(map(int, input().split()))

left = 0
right = n - 1
moves = 0

for i in range(n):
    moves += abs(a[i] - (i + 1))
    if a[i] < i + 1:
        left += 1
    if a[i] > i + 1:
        right += 1

print(moves + left + right)
