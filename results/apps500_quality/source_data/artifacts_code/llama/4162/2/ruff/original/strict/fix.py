
n = int(input())
a = list(map(int, input().split()))

max_sum = 0

for m in range(1, 10**5 * n):
    total = sum(m % ai for ai in a)
    if total > max_sum:
        max_sum = total

print(max_sum)
