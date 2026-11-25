
n, a = int(input()), list(map(int, input().split()))

max_p = 0
count = 0
for  i in  range(1, n):
    num, p = a[i], 0
    while num % (2 ** p) == 0:
        p = p + 1
    max_p = max(max_p, p)

for  i in  range(n):
    p, num = 0, a[i]
    while num % (2 ** p) == 0:
        p = p + 1
    if  p == max_p:
        count += 1

print(2 ** max_p, count)
