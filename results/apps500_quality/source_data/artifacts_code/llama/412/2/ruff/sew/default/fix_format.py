n = int(input())
a = list(map(int, input().split()))

max_div = count = 0

for i in range(n):
    num, exp = a[i], 0
    while num % 2 == 0:
        num = num // 2
        exp = exp + 1
    if max_div < exp:
        max_div = exp
        count = 1
    elif exp == max_div:
        count += 1

print(max_div, count)
