n = int(input())
count = 0
for i in range(1, 1 + n):
    is_divisible = False
    for j in range(2, 11):
        if i % j == 0:
            is_divisible = True
            break
    if is_divisible:
        count += 1
print(n - count)
