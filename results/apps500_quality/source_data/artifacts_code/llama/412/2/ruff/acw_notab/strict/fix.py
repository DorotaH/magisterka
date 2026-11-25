
n = int(input())
a = list(map(int, input().split()))

max_div = 0
count = 0

for i in range(n):
    num = a[i]
    exp = 0
    while num % 2 == 0:
        num //= 2
        exp += 1
    if exp > max_div:
        max_div = exp
        count = 1
    elif exp == max_div:
        count += 1

print(max_div, count)
